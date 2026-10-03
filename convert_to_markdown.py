import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import re
import fitz
import pytesseract
from PIL import Image
import io
import concurrent.futures

os.environ['TESSDATA_PREFIX'] = r'e:\DeThiChuyenTin\tessdata'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def convert_pdf_to_text(pdf_path):
    if not os.path.exists(pdf_path):
        return None
        
    doc = fitz.open(pdf_path)
    page_texts = []
    
    for i, page in enumerate(doc):
        raw = page.get_text().strip()
        # If native text is clean and substantial
        if len(raw) > 150:
            page_texts.append(raw)
        else:
            # Fallback to OCR
            try:
                mat = fitz.Matrix(2.0, 2.0)
                pix = page.get_pixmap(matrix=mat)
                img = Image.open(io.BytesIO(pix.tobytes('png')))
                ocr = pytesseract.image_to_string(img, lang='vie+eng')
                page_texts.append(ocr.strip())
            except Exception as e:
                page_texts.append(f"[Lỗi OCR trang {i+1}: {e}]")
                
    full_text = "\n\n".join(page_texts)
    return full_text

def format_exam_markdown(province, school, year, title, raw_text):
    md_lines = []
    md_lines.append(f"# {title}")
    md_lines.append("")
    md_lines.append(f"- **Tỉnh/Thành phố:** {province}")
    md_lines.append(f"- **Trường:** {school}")
    md_lines.append(f"- **Năm học:** {year}")
    md_lines.append(f"- **Môn thi:** Tin học (Chuyên)")
    md_lines.append("")
    md_lines.append("---")
    md_lines.append("")
    md_lines.append("## NỘI DUNG ĐỀ THI")
    md_lines.append("")
    
    # Clean up and normalize lines
    lines = raw_text.split('\n')
    cleaned_lines = []
    for line in lines:
        l_strip = line.strip()
        if not l_strip:
            cleaned_lines.append("")
            continue
            
        # Detect problem headers: Bài 1, Câu 1, BÀI 1, etc.
        if re.match(r'^(bài|câu|problem)\s+\d+[:.]?', l_strip, re.IGNORECASE):
            cleaned_lines.append("")
            cleaned_lines.append(f"### {l_strip}")
            cleaned_lines.append("")
        elif re.match(r'^(dữ liệu vào|input|dữ liệu ra|output|yêu cầu|ràng buộc|giới hạn|ví dụ|example)[:.]?', l_strip, re.IGNORECASE):
            cleaned_lines.append("")
            cleaned_lines.append(f"#### {l_strip}")
            cleaned_lines.append("")
        else:
            cleaned_lines.append(l_strip)
            
    md_lines.append("\n".join(cleaned_lines))
    return "\n".join(md_lines)

def process_single_exam(row_info, dethi_dir, md_dir):
    province = row_info['province']
    school = row_info['school']
    year = row_info['year']
    title = row_info['title']
    pdf_filename = row_info['pdf_filename']
    
    pdf_path = os.path.join(dethi_dir, pdf_filename)
    md_filename = os.path.splitext(pdf_filename)[0] + '.md'
    md_path = os.path.join(md_dir, md_filename)
    
    print(f"Processing: {pdf_filename}...")
    raw_text = convert_pdf_to_text(pdf_path)
    
    if raw_text:
        md_content = format_exam_markdown(province, school, year, title, raw_text)
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        return {
            'success': True,
            'md_filename': md_filename,
            'md_path': md_path
        }
    else:
        return {
            'success': False,
            'error': 'Could not extract text'
        }

def main():
    base_dir = r'e:\DeThiChuyenTin'
    dethi_dir = os.path.join(base_dir, 'dethi')
    md_dir = os.path.join(base_dir, 'dethi_markdown')
    os.makedirs(md_dir, exist_ok=True)
    
    md_file_path = os.path.join(base_dir, 'DanhSach_DeThi_ChuyenTin.md')
    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
        
    lines = md_content.split('\n')
    header_idx = -1
    for i, line in enumerate(lines):
        if line.startswith('| Tên Tỉnh |'):
            header_idx = i
            break
            
    if header_idx == -1:
        print("Header not found!")
        return

    table_rows = []
    for i in range(header_idx + 2, len(lines)):
        line = lines[i].strip()
        if not line.startswith('|') or not line.endswith('|'):
            break
        parts = [p.strip() for p in line.split('|')[1:-1]]
        if len(parts) >= 5:
            table_rows.append({
                'line_idx': i,
                'province': parts[0],
                'school': parts[1],
                'year': parts[2],
                'link': parts[3],
                'downloaded': parts[4]
            })

    print(f"Total table rows: {len(table_rows)}")
    
    # Filter downloaded rows
    downloaded_rows = []
    for r in table_rows:
        # Check if downloaded has pdf link
        pdf_match = re.search(r'\[([^\]]+\.pdf)\]', r['downloaded'])
        if pdf_match:
            r['pdf_filename'] = pdf_match.group(1)
            # Extract title from link
            title_match = re.search(r'\[Xem đề thi:\s*([^\]]+)\]', r['link'])
            r['title'] = title_match.group(1) if title_match else f"Đề thi {r['province']} {r['year']}"
            downloaded_rows.append(r)

    print(f"Total downloaded rows: {len(downloaded_rows)}")
    
    # Target first 50 downloaded exams
    target_50 = downloaded_rows[:50]
    print(f"Converting first {len(target_50)} exams...")
    
    converted_count = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        future_to_row = {executor.submit(process_single_exam, r, dethi_dir, md_dir): r for r in target_50}
        for future in concurrent.futures.as_completed(future_to_row):
            r = future_to_row[future]
            res = future.result()
            if res['success']:
                converted_count += 1
                r['md_filename'] = res['md_filename']
                print(f"[CONVERTED {converted_count}/50] {res['md_filename']}")
            else:
                r['md_filename'] = None
                print(f"[FAILED] {r['pdf_filename']}: {res.get('error')}")

    # Now update DanhSach_DeThi_ChuyenTin.md with new column "Đề thi markdown"
    new_lines = []
    # Lines before table
    for i in range(header_idx):
        new_lines.append(lines[i])
        
    # Table header
    new_lines.append("| Tên Tỉnh | Tên Trường | Năm học | Link đề thi | Đã tải | Đề thi markdown |")
    new_lines.append("| :--- | :--- | :---: | :--- | :---: | :--- |")
    
    # Table rows
    target_map = {r['line_idx']: r for r in target_50}
    for r in table_rows:
        prov = r['province']
        school = r['school']
        year = r['year']
        link = r['link']
        downloaded = r['downloaded']
        
        md_col = "[ ]"
        if r['line_idx'] in target_map:
            t_row = target_map[r['line_idx']]
            if t_row.get('md_filename'):
                md_fname = t_row['md_filename']
                md_col = f"[x] ([{md_fname}](file:///dethi_markdown/{md_fname}))"
                
        new_lines.append(f"| {prov} | {school} | {year} | {link} | {downloaded} | {md_col} |")

    # Lines after table
    after_table = False
    for i in range(header_idx + 2 + len(table_rows), len(lines)):
        new_lines.append(lines[i])
        
    new_lines.append(f"- **Đã convert sang Markdown (`/dethi_markdown`):** **{converted_count}** / 50 đề thi đầu tiên.")

    with open(md_file_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))

    print(f"\nDone! Converted {converted_count} exams to Markdown and updated {md_file_path}")

if __name__ == '__main__':
    main()
