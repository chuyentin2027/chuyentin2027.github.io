import json
import re
import unicodedata

def normalize_text(text):
    nfc = unicodedata.normalize('NFC', text).lower()
    # Normalize variants
    nfc = re.sub(r'\s+', ' ', nfc)
    nfc = nfc.replace('kom tum', 'kon tum').replace('dak lak', 'đắk lắk').replace('daklak', 'đắk lắk').replace('ak lak', 'đắk lắk')
    return nfc

with open('e:/DeThiChuyenTin/verified_exams.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

provinces_map = [
    ('phổ thông năng khiếu', 'TP. Hồ Chí Minh', 'Trường Phổ thông Năng khiếu (ĐHQG-HCM)'),
    ('ptnk', 'TP. Hồ Chí Minh', 'Trường Phổ thông Năng khiếu (ĐHQG-HCM)'),
    ('sư phạm hà nội', 'Hà Nội', 'THPT Chuyên Đại học Sư phạm Hà Nội'),
    ('đại học sư phạm', 'Hà Nội', 'THPT Chuyên Đại học Sư phạm Hà Nội'),
    ('chuyên đại học sư phạm', 'Hà Nội', 'THPT Chuyên Đại học Sư phạm Hà Nội'),
    ('khoa học tự nhiên hà nội', 'Hà Nội', 'THPT Chuyên Khoa học Tự nhiên (ĐHKHTN - ĐHQGHN)'),
    ('đại học khoa học tự nhiên', 'Hà Nội', 'THPT Chuyên Khoa học Tự nhiên (ĐHKHTN - ĐHQGHN)'),
    ('chuyên khoa học tự nhiên', 'Hà Nội', 'THPT Chuyên Khoa học Tự nhiên (ĐHKHTN - ĐHQGHN)'),
    ('đại học vinh', 'Nghệ An', 'THPT Chuyên Đại học Vinh'),
    ('đại học khoa học - huế', 'Thừa Thiên Huế', 'THPT Chuyên Khoa học Huế'),
    ('đại học khoa học huế', 'Thừa Thiên Huế', 'THPT Chuyên Khoa học Huế'),
    ('hà nội', 'Hà Nội', 'THPT Chuyên Hà Nội - Amsterdam / THPT Chuyên Nguyễn Huệ'),
    ('hồ chí minh', 'TP. Hồ Chí Minh', 'THPT Chuyên Lê Hồng Phong / THPT Chuyên Trần Đại Nghĩa'),
    ('tphcm', 'TP. Hồ Chí Minh', 'THPT Chuyên Lê Hồng Phong / THPT Chuyên Trần Đại Nghĩa'),
    ('lê hồng phong - nam định', 'Nam Định', 'THPT Chuyên Lê Hồng Phong'),
    ('lê hồng phong', 'TP. Hồ Chí Minh', 'THPT Chuyên Lê Hồng Phong'),
    ('hải phòng', 'Hải Phòng', 'THPT Chuyên Trần Phú'),
    ('trần phú', 'Hải Phòng', 'THPT Chuyên Trần Phú'),
    ('quảng ninh', 'Quảng Ninh', 'THPT Chuyên Hạ Long'),
    ('hạ long', 'Quảng Ninh', 'THPT Chuyên Hạ Long'),
    ('hải dương', 'Hải Dương', 'THPT Chuyên Nguyễn Trãi'),
    ('nguyễn trãi', 'Hải Dương', 'THPT Chuyên Nguyễn Trãi'),
    ('bắc ninh', 'Bắc Ninh', 'THPT Chuyên Bắc Ninh'),
    ('hưng yên', 'Hưng Yên', 'THPT Chuyên Hưng Yên'),
    ('nam định', 'Nam Định', 'THPT Chuyên Lê Hồng Phong'),
    ('thái bình', 'Thái Bình', 'THPT Chuyên Thái Bình'),
    ('hà nam', 'Hà Nam', 'THPT Chuyên Biên Hòa'),
    ('biên hòa', 'Hà Nam', 'THPT Chuyên Biên Hòa'),
    ('ninh bình', 'Ninh Bình', 'THPT Chuyên Lương Văn Tụy'),
    ('lương văn tụy', 'Ninh Bình', 'THPT Chuyên Lương Văn Tụy'),
    ('vĩnh phúc', 'Vĩnh Phúc', 'THPT Chuyên Vĩnh Phúc'),
    ('phú thọ', 'Phú Thọ', 'THPT Chuyên Hùng Vương'),
    ('hùng vương', 'Phú Thọ', 'THPT Chuyên Hùng Vương'),
    ('bắc giang', 'Bắc Giang', 'THPT Chuyên Bắc Giang'),
    ('thái nguyên', 'Thái Nguyên', 'THPT Chuyên Thái Nguyên'),
    ('lạng sơn', 'Lạng Sơn', 'THPT Chuyên Chu Văn An'),
    ('cao bằng', 'Cao Bằng', 'THPT Chuyên Cao Bằng'),
    ('bắc kạn', 'Bắc Kạn', 'THPT Chuyên Bắc Kạn'),
    ('tuyên quang', 'Tuyên Quang', 'THPT Chuyên Tuyên Quang'),
    ('hà giang', 'Hà Giang', 'THPT Chuyên Hà Giang'),
    ('lào cai', 'Lào Cai', 'THPT Chuyên Lào Cai'),
    ('yên bái', 'Yên Bái', 'THPT Chuyên Nguyễn Tất Thành'),
    ('hòa bình', 'Hòa Bình', 'THPT Chuyên Hoàng Văn Thụ'),
    ('hoàng văn thụ', 'Hòa Bình', 'THPT Chuyên Hoàng Văn Thụ'),
    ('sơn la', 'Sơn La', 'THPT Chuyên Sơn La'),
    ('điện biên', 'Điện Biên', 'THPT Chuyên Lê Quý Đôn'),
    ('lai châu', 'Lai Châu', 'THPT Chuyên Lê Quý Đôn'),
    ('thanh hóa', 'Thanh Hóa', 'THPT Chuyên Lam Sơn'),
    ('lam sơn', 'Thanh Hóa', 'THPT Chuyên Lam Sơn'),
    ('nghệ an', 'Nghệ An', 'THPT Chuyên Phan Bội Châu'),
    ('phan bội châu', 'Nghệ An', 'THPT Chuyên Phan Bội Châu'),
    ('hà tĩnh', 'Hà Tĩnh', 'THPT Chuyên Hà Tĩnh'),
    ('quảng bình', 'Quảng Bình', 'THPT Chuyên Võ Nguyên Giáp'),
    ('võ nguyên giáp', 'Quảng Bình', 'THPT Chuyên Võ Nguyên Giáp'),
    ('quảng trị', 'Quảng Trị', 'THPT Chuyên Lê Quý Đôn'),
    ('thừa thiên huế', 'Thừa Thiên Huế', 'THPT Chuyên Quốc Học Huế'),
    ('quốc học huế', 'Thừa Thiên Huế', 'THPT Chuyên Quốc Học Huế'),
    ('huế', 'Thừa Thiên Huế', 'THPT Chuyên Quốc Học Huế'),
    ('đà nẵng', 'Đà Nẵng', 'THPT Chuyên Lê Quý Đôn'),
    ('quảng nam', 'Quảng Nam', 'THPT Chuyên Nguyễn Bỉnh Khiêm / THPT Chuyên Lê Thánh Tông'),
    ('quảng ngãi', 'Quảng Ngãi', 'THPT Chuyên Lê Khiết'),
    ('lê khiết', 'Quảng Ngãi', 'THPT Chuyên Lê Khiết'),
    ('bình định', 'Bình Định', 'THPT Chuyên Lê Quý Đôn / THPT Chuyên Chu Văn An'),
    ('phú yên', 'Phú Yên', 'THPT Chuyên Lương Văn Chánh'),
    ('lương văn chánh', 'Phú Yên', 'THPT Chuyên Lương Văn Chánh'),
    ('khánh hòa', 'Khánh Hòa', 'THPT Chuyên Lê Quý Đôn'),
    ('ninh thuận', 'Ninh Thuận', 'THPT Chuyên Lê Quý Đôn'),
    ('bình thuận', 'Bình Thuận', 'THPT Chuyên Trần Hưng Đạo'),
    ('trần hưng đạo', 'Bình Thuận', 'THPT Chuyên Trần Hưng Đạo'),
    ('kon tum', 'Kon Tum', 'THPT Chuyên Nguyễn Tất Thành'),
    ('gia lai', 'Gia Lai', 'THPT Chuyên Hùng Vương'),
    ('đắk lắk', 'Đắk Lắk', 'THPT Chuyên Nguyễn Du'),
    ('đắk nông', 'Đắk Nông', 'THPT Chuyên Nguyễn Chí Thanh'),
    ('nguyễn chí thanh', 'Đắk Nông', 'THPT Chuyên Nguyễn Chí Thanh'),
    ('lâm đồng', 'Lâm Đồng', 'THPT Chuyên Thăng Long / THPT Chuyên Bảo Lộc'),
    ('bình dương', 'Bình Dương', 'THPT Chuyên Hùng Vương'),
    ('bình phước', 'Bình Phước', 'THPT Chuyên Quang Trung / THPT Chuyên Bình Long'),
    ('đồng nai', 'Đồng Nai', 'THPT Chuyên Lương Thế Vinh'),
    ('lương thế vinh', 'Đồng Nai', 'THPT Chuyên Lương Thế Vinh'),
    ('tây ninh', 'Tây Ninh', 'THPT Chuyên Hoàng Lê Kha'),
    ('hoàng lê kha', 'Tây Ninh', 'THPT Chuyên Hoàng Lê Kha'),
    ('bà rịa', 'Bà Rịa - Vũng Tàu', 'THPT Chuyên Lê Quý Đôn'),
    ('vũng tàu', 'Bà Rịa - Vũng Tàu', 'THPT Chuyên Lê Quý Đôn'),
    ('long an', 'Long An', 'THPT Chuyên Long An'),
    ('tiền giang', 'Tiền Giang', 'THPT Chuyên Tiền Giang'),
    ('bến tre', 'Bến Tre', 'THPT Chuyên Bến Tre'),
    ('đồng tháp', 'Đồng Tháp', 'THPT Chuyên Nguyễn Quang Diêu / THPT Chuyên Nguyễn Đình Chiểu'),
    ('nguyễn quang diêu', 'Đồng Tháp', 'THPT Chuyên Nguyễn Quang Diêu'),
    ('vĩnh long', 'Vĩnh Long', 'THPT Chuyên Nguyễn Bỉnh Khiêm'),
    ('trà vinh', 'Trà Vinh', 'THPT Chuyên Trà Vinh'),
    ('an giang', 'An Giang', 'THPT Chuyên Thoại Ngọc Hầu / THPT Chuyên Thủ Khoa Nghĩa'),
    ('cần thơ', 'Cần Thơ', 'THPT Chuyên Lý Tự Trọng'),
    ('lý tự trọng', 'Cần Thơ', 'THPT Chuyên Lý Tự Trọng'),
    ('hậu giang', 'Hậu Giang', 'THPT Chuyên Vị Thanh'),
    ('sóc trăng', 'Sóc Trăng', 'THPT Chuyên Nguyễn Thị Minh Khai'),
    ('bạc liêu', 'Bạc Liêu', 'THPT Chuyên Bạc Liêu'),
    ('cà mau', 'Cà Mau', 'THPT Chuyên Phan Ngọc Hiển'),
    ('kiên giang', 'Kiên Giang', 'THPT Chuyên Huỳnh Mẫn Đạt'),
    ('huỳnh mẫn đạt', 'Kiên Giang', 'THPT Chuyên Huỳnh Mẫn Đạt'),
]

parsed_rows = []
seen_keys = set()

for it in items:
    title = it['title'].strip()
    url = it['url'].strip()
    t_norm = normalize_text(title)
    
    # Filter out non-exam entries
    if any(k in t_norm for k in ['khai giảng', 'thông báo tuyển sinh', 'tài liệu ôn', 'gói luyện giải', 'ôn thi lớp 10', 'tổng hợp đề thi']):
        continue
    
    # Extract School Year
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

    # Detect Province & School
    matched_prov = None
    matched_school = None
    
    for key, p_name, s_name in provinces_map:
        if normalize_text(key) in t_norm:
            matched_prov = p_name
            matched_school = s_name
            break
            
    if not matched_prov:
        matched_prov = "Toàn quốc"
        matched_school = "THPT Chuyên (Đề thi thử chung)"
        
    dedup_key = (matched_prov, matched_school, year_str, url)
    if dedup_key not in seen_keys:
        seen_keys.add(dedup_key)
        parsed_rows.append({
            'province': matched_prov,
            'school': matched_school,
            'year': year_str,
            'title': title,
            'url': url
        })

# Sort by Province, then School, then Year descending
parsed_rows.sort(key=lambda x: (x['province'] == 'Toàn quốc', x['province'], x['school'], x['year']))

# Build Markdown content
lines = []
lines.append("# DANH SÁCH ĐỀ THI TUYỂN SINH VÀO LỚP 10 CHUYÊN TIN HỌC (STATUS 200 OK)")
lines.append("")
lines.append("> Danh sách đã được rà soát và kiểm tra tự động: **100% liên kết hoạt động (HTTP Status 200 OK)**, chỉ bao gồm đề thi tuyển sinh đầu vào lớp 10 Chuyên Tin học.")
lines.append("")
lines.append("| Tên Tỉnh | Tên Trường | Năm học | Link đề thi |")
lines.append("| :--- | :--- | :---: | :--- |")

for r in parsed_rows:
    lines.append(f"| {r['province']} | {r['school']} | {r['year']} | [Xem đề thi: {r['title']}]({r['url']}) |")

lines.append("")
lines.append(f"*Tổng số đề thi chuyên Tin hoạt động đã xác thực: **{len(parsed_rows)}** đề.*")

with open('e:/DeThiChuyenTin/DanhSach_DeThi_ChuyenTin.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f"Successfully generated {len(parsed_rows)} rows in DanhSach_DeThi_ChuyenTin.md")
