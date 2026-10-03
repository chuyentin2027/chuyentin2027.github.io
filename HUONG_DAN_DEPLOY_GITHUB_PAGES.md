# HƯỚNG DẪN TRIỂN KHAI HỆ THỐNG ĐỀ THI LÊN GITHUB PAGES + SUPABASE (100% MIỄN PHÍ)

Hệ thống cho phép bạn đưa trang web lên Internet miễn phí vĩnh viễn, học sinh ở bất cứ đâu đều có thể truy cập, xem đề thi PDF trực tuyến và gửi/xem code Python lời giải theo thời gian thực (Realtime).

---

## BƯỚC 1: TẠO DATABASE MIỄN PHÍ TRÊN SUPABASE (2 phút)

1. Truy cập [https://supabase.com](https://supabase.com) và đăng ký tài khoản miễn phí (bằng tài khoản GitHub hoặc Google).
2. Bấm **"New project"**, đặt tên project (ví dụ: `DeThiChuyenTin`), chọn mật khẩu database và chọn Region (ví dụ: `Singapore` để có tốc độ nhanh nhất tại Việt Nam).
3. Sau khi tạo xong:
   - Vào mục **SQL Editor** ở thanh menu bên trái.
   - Bấm **"New query"**, mở file [supabase_setup.sql](file:///e:/DeThiChuyenTin/supabase_setup.sql), copy toàn bộ nội dung dán vào và bấm **"Run"**. (Lệnh này sẽ tạo bảng `exam_solutions` và phân quyền cho học sinh nộp bài công khai).
4. Lấy thông tin API:
   - Vào mục **Project Settings (Bánh răng) -> API**.
   - Copy **Project URL** (ví dụ: `https://xyzabcdef.supabase.co`).
   - Copy **anon public Key** (chuỗi ký tự dài bắt đầu bằng `eyJ...`).
5. Mở file [config.js](file:///e:/DeThiChuyenTin/config.js) trong thư mục dự án và dán 2 thông tin trên vào:
   ```javascript
   window.SUPABASE_CONFIG = {
       url: "https://xyzabcdef.supabase.co", 
       anonKey: "eyJhbGciOi..."
   };
   ```

*(Lưu ý: Nếu chưa cấu hình Supabase, hệ thống vẫn hoạt động bình thường và lưu bài nộp vào bộ nhớ trình duyệt LocalStorage).*

---

## BƯỚC 2: ĐẨY TOÀN BỘ CODE LÊN GITHUB

1. Truy cập [https://github.com](https://github.com) và tạo một Repository mới (ví dụ đặt tên là `DeThiChuyenTin`), chọn chế độ **Public**.
2. Mở Terminal (PowerShell hoặc Git Bash) tại thư mục `e:\DeThiChuyenTin` và chạy các lệnh sau:

```bash
git init
git add .
git commit -m "Kho de thi chuyen tin va loi giai Python"
git branch -M main
git remote add origin https://github.com/<TEN_TAI_KHOAN_GITHUB_CUA_BAN>/DeThiChuyenTin.git
git push -u origin main
```

---

## BƯỚC 3: BẬT TÍNH NĂNG GITHUB PAGES

1. Trên giao diện Repository của bạn trên GitHub, vào mục **Settings** -> chọn menu **Pages** bên cột trái.
2. Tại mục **Build and deployment -> Source**, chọn **Deploy from a branch**.
3. Tại mục **Branch**, chọn nhánh `main` và thư mục `/ (root)` -> Bấm **Save**.
4. Chờ khoảng 1 - 2 phút, GitHub sẽ cung cấp cho bạn link trang web trực tuyến:
   👉 **`https://<TEN_TAI_KHOAN_GITHUB_CUA_BAN>.github.io/DeThiChuyenTin/`**

---

## BƯỚC 4: HỌC SINH SỬ DỤNG NHƯ THẾ NÀO?

- Học sinh chỉ cần click vào link web trên:
  1. Tra cứu đề theo Tỉnh, Trường hoặc Năm học.
  2. Bấm **"Xem PDF"** để xem trực tiếp đề thi toàn màn hình.
  3. Bấm **"Lời giải"** hoặc chuyển sang chế độ **"Chia Đôi (Split View)"** để vừa đọc đề vừa xem các bài giải Python đã có.
  4. Bấm **"Nộp code mới"** để viết code Python (có sẵn phím Tab thụt 4 spaces, font code chuyên dụng, tô màu cú pháp chuẩn) và gửi lên Cloud cho cả lớp cùng xem.
