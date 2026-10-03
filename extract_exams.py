import sys
import urllib.request
import json
import ssl
import re

sys.stdout.reconfigure(encoding='utf-8')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

all_posts = []
start = 1
while True:
    url = f'https://www.chuyentin.pro/feeds/posts/default?alt=json&start-index={start}&max-results=150'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            entries = data.get('feed', {}).get('entry', [])
            if not entries:
                break
            for entry in entries:
                title = entry.get('title', {}).get('$t', '')
                links = entry.get('link', [])
                alt = [l['href'] for l in links if l.get('rel') == 'alternate']
                if alt:
                    all_posts.append({'title': title, 'url': alt[0]})
            start += len(entries)
            if len(entries) < 150:
                break
    except Exception as e:
        print('Fetch Error:', e)
        break

print(f'Total posts fetched: {len(all_posts)}')

# Filter strictly for Grade 10 specialized informatics entrance exams
grade10_exams = []
for p in all_posts:
    t = p['title'].lower()
    
    # Must be entrance to grade 10 / vao 10 / tuyen sinh 10
    is_tuyensinh = any(k in t for k in ['tuyển sinh lớp 10', 'tuyển sinh vào lớp 10', 'vào 10', 'vào lớp 10', 'tuyển sinh 10', 'lớp 10 chuyên tin', 'lớp 10 thpt chuyên'])
    
    # Exclude other grades / competitions
    is_not_other = not any(k in t for k in ['lớp 9', 'lớp 12', 'lớp 11', 'khối 11', 'khối 12', 'khối 9', 'quốc gia', 'tiểu học', 'thcs', 'bảng a', 'bảng b', 'bảng d', 'bảng c', 'icpc', 'vnoicup', 'duyên hải', 'hsg qg', 'học sinh giỏi'])
    
    if is_tuyensinh and is_not_other:
        grade10_exams.append(p)

print(f'Found {len(grade10_exams)} Grade 10 entrance exams.')

# Check HTTP 200 for all found URLs
verified = []
for item in grade10_exams:
    url = item['url']
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=5) as resp:
            if resp.status == 200:
                verified.append(item)
                print(f"[200 OK] {item['title']} -> {url}")
            else:
                print(f"[{resp.status}] {item['title']} -> {url}")
    except Exception as e:
        print(f"[ERR {e}] {item['title']} -> {url}")

with open('e:/DeThiChuyenTin/verified_exams.json', 'w', encoding='utf-8') as f:
    json.dump(verified, f, ensure_ascii=False, indent=2)

print(f'Done. Total verified live Grade 10 entrance exams: {len(verified)}')
