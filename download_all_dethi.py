import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import re
import ssl
import json
import urllib.request
import unicodedata
import io
from PIL import Image
from concurrent.futures import ThreadPoolExecutor, as_completed
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

def sanitize_filename(text):
    nfkd = unicodedata.normalize('NFKD', text)
    ascii_text = ''.join([c for c in nfkd if not unicodedata.combining(c)])
    ascii_text = re.sub(r'[^a-zA-Z0-9_-]', '_', ascii_text)
    ascii_text = re.sub(r'_+', '_', ascii_text).strip('_')
    return ascii_text[:80]

def extract_download_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    candidates = []
    
    # 1. Look for iframes / embeds / direct links
    for tag in soup.find_all(['iframe', 'embed', 'a']):
        src = tag.get('src') or tag.get('href')
        if not src:
            continue
        
        # Google Drive file
        drive_match = re.search(r'drive\.google\.com/file/d/([a-zA-Z0-9_-]+)', src)
        if drive_match:
            file_id = drive_match.group(1)
            candidates.append(('drive_file', file_id, f'https://drive.usercontent.google.com/download?id={file_id}&export=download'))
            continue
            
        # Google Docs
        docs_match = re.search(r'docs\.google\.com/document/d/([a-zA-Z0-9_-]+)', src)
        if docs_match:
            doc_id = docs_match.group(1)
            candidates.append(('google_doc', doc_id, f'https://docs.google.com/document/d/{doc_id}/export?format=pdf'))
            continue
            
        # Direct PDF
        if '.pdf' in src.lower() and ('http://' in src or 'https://' in src):
            candidates.append(('direct_pdf', None, src))
            
    return candidates

def extract_post_images(html):
    soup = BeautifulSoup(html, 'html.parser')
    post_body = soup.find(class_=re.compile(r'post-body|entry-content')) or soup
    img_urls = []
    for img in post_body.find_all('img'):
        src = img.get('src')
        if not src:
            continue
        # Filter out avatars, icons, banners
        if any(skip in src for skip in ['s240', 's72', 'w72', 'avatar', 'icon', 'banner', 'button']):
            continue
        # If blogger image, get high res (replace /sxxx/ or /wxxx/ with /s0/)
        high_res = re.sub(r'/(s\d+|w\d+-h\d+[^/]*)/', '/s0/', src)
        img_urls.append(high_res)
    return img_urls

def images_to_pdf(img_urls, out_pdf):
    pil_images = []
    for u in img_urls:
        try:
            req = urllib.request.Request(u, headers=HEADERS)
            with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
                data = resp.read()
                img = Image.open(io.BytesIO(data))
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                pil_images.append(img)
        except Exception:
            continue
            
    if pil_images:
        pil_images[0].save(out_pdf, save_all=True, append_images=pil_images[1:])
        return True
    return False

def download_item(item, output_dir):
    prov = item['province']
    school = item['school']
    year = item['year']
    title = item['title']
    page_url = item['url']
    
    base_name = f"{sanitize_filename(prov)}_{sanitize_filename(year)}_{sanitize_filename(title)}"
    out_pdf = os.path.join(output_dir, f"{base_name}.pdf")
    
    result = {
        'province': prov,
        'school': school,
        'year': year,
        'title': title,
        'url': page_url,
        'downloaded': False,
        'file_path': None,
        'error': None
    }
    
    if os.path.exists(out_pdf) and os.path.getsize(out_pdf) > 2000:
        result['downloaded'] = True
        result['file_path'] = os.path.relpath(out_pdf, 'e:/DeThiChuyenTin')
        return result
        
    try:
        req = urllib.request.Request(page_url, headers=HEADERS)
        with urllib.request.urlopen(req, context=ctx, timeout=12) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            
        candidates = extract_download_links(html)
        
        # 1. Try candidates from drive / docs / pdf
        for kind, fid, d_url in candidates:
            try:
                d_req = urllib.request.Request(d_url, headers=HEADERS)
                with urllib.request.urlopen(d_req, context=ctx, timeout=20) as d_resp:
                    content = d_resp.read()
                    
                if len(content) > 1000:
                    if content.startswith(b'<!DOCTYPE html') and b'Google Drive - Virus scan warning' not in content:
                        if b'confirm=' in content or b'download_warning' in content:
                            alt_url = f"https://drive.google.com/uc?export=download&id={fid}"
                            with urllib.request.urlopen(urllib.request.Request(alt_url, headers=HEADERS), context=ctx, timeout=20) as a_resp:
                                content = a_resp.read()
                                
                    if len(content) > 2000 and not (content.startswith(b'<!DOCTYPE html') and b'<html' in content.lower() and len(content) < 10000):
                        with open(out_pdf, 'wb') as f:
                            f.write(content)
                        result['downloaded'] = True
                        result['file_path'] = os.path.relpath(out_pdf, 'e:/DeThiChuyenTin')
                        return result
            except Exception:
                continue
                
        # 2. If no candidate succeeded, try extracting post images and convert to PDF
        post_imgs = extract_post_images(html)
        if post_imgs and images_to_pdf(post_imgs, out_pdf):
            result['downloaded'] = True
            result['file_path'] = os.path.relpath(out_pdf, 'e:/DeThiChuyenTin')
            return result
            
        result['error'] = 'No downloadable files or images found'
    except Exception as e:
        result['error'] = str(e)
        
    return result

def main():
    output_dir = 'e:/DeThiChuyenTin/dethi'
    os.makedirs(output_dir, exist_ok=True)
    
    with open('e:/DeThiChuyenTin/verified_exams.json', 'r', encoding='utf-8') as f:
        items = json.load(f)
        
    from build_markdown import provinces_map, normalize_text
    
    parsed_items = []
    seen = set()
    for it in items:
        title = it['title'].strip()
        url = it['url'].strip()
        t_norm = normalize_text(title)
        
        if any(k in t_norm for k in ['khai giảng', 'thông báo tuyển sinh', 'tài liệu ôn', 'gói luyện giải', 'ôn thi lớp 10', 'tổng hợp đề thi']):
            continue
            
        year_match = re.search(r'(\d{4})\s*-\s*(\d{4})', title)
        year_str = ""
        if year_match:
            y1, y2 = year_match.group(1), year_match.group(2)
            if int(y1) >= 2019:
                year_str = f"{y1} - {y2}"
        else:
            single_year = re.search(r'202[0-6]|2019', title)
            if single_year:
                y = int(single_year.group(0))
                year_str = f"{y} - {y+1}"
                
        if not year_str:
            continue
            
        matched_prov = "Toàn quốc"
        matched_school = "THPT Chuyên (Đề thi thử chung)"
        for key, p_name, s_name in provinces_map:
            if normalize_text(key) in t_norm:
                matched_prov = p_name
                matched_school = s_name
                break
                
        key = (matched_prov, matched_school, year_str, url)
        if key not in seen:
            seen.add(key)
            parsed_items.append({
                'province': matched_prov,
                'school': matched_school,
                'year': year_str,
                'title': title,
                'url': url
            })

    print(f"Starting download for {len(parsed_items)} exam papers...")
    
    results = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(download_item, it, output_dir): it for it in parsed_items}
        for future in as_completed(futures):
            res = future.result()
            results.append(res)
            status_str = "[OK]" if res['downloaded'] else f"[FAIL: {res['error']}]"
            print(f"{status_str} {res['province']} - {res['title'][:50]}")

    # Sort results
    results.sort(key=lambda x: (x['province'] == 'Toàn quốc', x['province'], x['school'], x['year']))
    
    # Generate updated Markdown with column 'Đã tải'
    lines = []
    lines.append("# DANH SÁCH ĐỀ THI TUYỂN SINH VÀO LỚP 10 CHUYÊN TIN HỌC (STATUS 200 OK)")
    lines.append("")
    lines.append("> Danh sách đã được rà soát và kiểm tra tự động: **100% liên kết hoạt động (HTTP Status 200 OK)**, chỉ bao gồm đề thi tuyển sinh đầu vào lớp 10 Chuyên Tin học.")
    lines.append("> Các đề thi đã được tự động dò tìm liên kết Google Drive / PDF / tài liệu đính kèm, tải về thư mục con `dethi/` và đánh dấu tích `[x]` tại cột **Đã tải**.")
    lines.append("")
    lines.append("| Tên Tỉnh | Tên Trường | Năm học | Link đề thi | Đã tải |")
    lines.append("| :--- | :--- | :---: | :--- | :---: |")

    success_count = 0
    for r in results:
        download_mark = "[ ]"
        if r['downloaded']:
            success_count += 1
            rel_f = r['file_path'].replace('\\', '/')
            file_name = os.path.basename(rel_f)
            download_mark = f"[x] ([{file_name}](file:///{rel_f}))"
            
        lines.append(f"| {r['province']} | {r['school']} | {r['year']} | [Xem đề thi: {r['title']}]({r['url']}) | {download_mark} |")

    lines.append("")
    lines.append(f"- **Tổng số đề thi chuyên Tin:** **{len(results)}** đề.")
    lines.append(f"- **Đã tải thành công về thư mục `/dethi`:** **{success_count}** / {len(results)} đề.")

    with open('e:/DeThiChuyenTin/DanhSach_DeThi_ChuyenTin.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f"\nCompleted! Downloaded {success_count}/{len(results)} files to {output_dir}")

if __name__ == '__main__':
    main()
