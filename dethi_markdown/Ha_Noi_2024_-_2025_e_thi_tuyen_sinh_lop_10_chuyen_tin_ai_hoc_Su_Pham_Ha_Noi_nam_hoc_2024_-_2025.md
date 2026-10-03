# Đề thi tuyển sinh lớp 10 chuyên tin Đại học Sư Phạm Hà Nội năm học 2024 - 2025

- **Tỉnh/Thành phố:** Hà Nội
- **Trường:** THPT Chuyên Đại học Sư phạm Hà Nội
- **Năm học:** 2024 - 2025
- **Môn thi:** Tin học (Chuyên)

---

## NỘI DUNG ĐỀ THI

BỘ GIÁO DỤC VÀ ĐÀO TẠO
TRUONG ĐẠI HỌC SƯ PHAM HÀ NỘI TRƯỜNG THPT CHUYEN ĐẠI H AMNĂM 2024

ĐÈ CHÍNH THỨC
(Đề thi gồm có 04 trang)

MÔN THI: TIN HỌC 22»
(Dùng riêng cho thi sinh thi vào lớp chuyên Tin học) ly
Thời gian lam bài: 120 phút (không kể thời gian phát dé) O

Tén bài Tên file bài làm _ | Giới hạn mỗi test
Tổng lớn nhất CAUI.* 1 giây/1 GB
Máy quét số CAU2.* 1 giây/1 GB
Trò chơi CAU3.* 1 giây/1 GB
Tìm số CAU4.* 1 giây/1 GB

Chú ý:


#### Dữ liệu vào đúng đắn không cân kiểm tra;


Dấu * được thay bằng cpp, e, pas, py tùy theo ngôn ngữ lập trình được sử dung (C++, C,
Pascal hay Python);

Chương trình sử dung cơ chế nhập/xuất dữ liệu từ thiết bị nhập chuẩn (standard input) và

thiết bị xuất chuẩn (standard output), không được phép doc/ghi bat kỳ tệp (file) nào trên
máy tính.

Cấu hình dịch để chấm bài:
C++ (GNU G++ 9.2): -std=c++14 -02 -s -static -lm -x c++
C (GNU GCC 9.2): -std=c11 -02 -s -static -lm -x c
Pascal (Free Pascal 3.0.4): -02 -XS -Sg
Python (Python 3): Chay trực tiếp mã nguồn qua thông dich

Hãy lập chương trình giải quyết các bài toán sau đây:

### Câu 1. TONG LỚN NHÁT (3.0 điểm) Tén chương trình: CAUI.*


Cho một số nguyên dương n (n > 3). Tìm số nguyên dương m (1 <m < m — 1) để tổng
GCD(m,n) + m dat giá trị lớn nhất. Với GCD(m, n) là ước chung lớn nhất của 2 số m và n. Nếu
có nhiều số m thỏa mãn thì đưa ra số m lớn nhất.

Dữ liệu: Vào từ thiết bị nhập chuẩn gồm số nguyên dương n (n < 101).

Kết quả: Ghỉ ra thiết bị xuất chuẩn gồm số nguyên dương m tìm được.


#### Ví dụ:


Sample Input Sample Output
15 12


#### Giới hạn:


© 60% số test ứng với n < 10!.
© 40% số test còn lại ứng với _n < 1014.

Trang 1⁄4

%

### Câu 2. MAY QUET SO (2.5 điểm) Tên chương trình: CAU2.*

Hệ thống máy quét để nhận dạng các số của một ngân hàng hiện đã bị hacker. nhập và
làm cho chúng không thể nhận dạng được một số chữ số. Tạm gọi những chữ số m ét
không nhận dạng được là chữ số bị hỏng. Máy quét sẽ không nhận dạng được các số có dưới
nhất một chữ số bị hỏng.
Vi dụ: Có 3 chữ số bị hỏng: 0, 1, 3 thì máy quét sẽ không nhận dạng được các số: VÔ)
1,3, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 30,... “©
Để đánh giá khả năng làm việc của máy quét, đội kiểm định đưa ra yêu cầu: biết các chữ số
bị hỏng và một số nguyên dương n cho trước, họ cần biết có bao nhiêu số nguyên dương không
vượt quá n mà máy quét vẫn có thể nhận dạng được.

Yéu cầu: Ban hãy giúp đội kiểm định tìm số lượng số nguyên dương không vượt quá n mà
máy quét vẫn nhận dạng được.
Dữ liệu: Vào từ thiết bị nhập chuẩn gồm:
© _ Dòng 1: gồm một số nguyên dương n(n < 107).
© Dong 2: gồm một xâu kí tự là các chữ số bị hỏng (độ dài xâu không vượt quá 10).
Các chữ số bị hỏng được viết liên tiếp không có dấu cách.
Kết quả: Ghi ra thiết bị xuất chuẩn một số nguyên duy nhất là số lượng các số nguyên dương
không vượt quá n mà máy quét có thé nhận dạng được.

#### Ví dụ: ___ _ —

Sample Tnput Sample Output Giai thich
30 14 Từ 1 tới 3Ø có 39 số nguyên dương.
310 Có 3 chữ số bị hỏng là: 3, 1, @ (hay chính
là: 0, 1, 3)
= Các số không nhận dạng được là: 1, 3,

10, 11, 12, 13, 14, 15, 16, 17, 18, 19
20, 21, 23, 3@ (16 số).

Còn lại: 39 - 16 = 14 số máy quét có thể
nhận dạng được.

199909
91256789

#### Giới hạn:

© 20% số test ứng với n < 10.
© 30% số test ứng khác với n < 105.
© _ 50% số test còn lại ứng với các test không có ràng buộc gì thêm.


### Câu 3. TRÒ CHƠI (2.5 điểm) Tén chương trình: CAU3.*

Tai giờ sinh hoạt cuối năm học, cô giáo tổ chức cho các bạn học sinh chơi trò choi.

“Trên bảng, có vẽ sẵn một hình chữ nhật kích thước 1 x n được chia thành n 6 vuông đơn vị.
Mỗi ô vuông có ghi một số nguyên dương. Ví dụ:

3 5 | 6|4 5 1

Trang 2/4

Cô đưa ra một số nguyên m và yêu cầu các bạn học sinh trong lớp 44 h tạo ra một
khung hình chữ nhật kích thước 1 x k đặt lên bảng sao cho khi trượt lần | ình chữ
nhật này từ trái qua phải, tổng các số trong dãy số lọt vào khung hình không, “/ hơn
giá trị m đã cho. ⁄

Bạn nào đưa ra được khung hình kích thước 1 x k với k nhỏ nhất thỏa mãn các yêu avy
cô giáo sẽ là người được nhận quà. +

Yéu cầu: Ban hãy giúp cô giáo tìm đáp số để xác định được sớm nhất học sinh làm đúng
yêu câu của cô.

Dữ liệu: Vào từ thiết bị nhập chuẩn gồm:

© Dòng đầu tiên chứa hai số nguyên n,m (1 <n < 105,1 <m < 10°)

© Dòng tiếp theo chứa lần lượt các số ay, đạ,..., đạ (1 < a; < 109) lần lượt là các số
được viết trên các ô vuông trên bảng.


#### Dữ liệu vào đảm bảo tổng của cả dãy không nhỏ hơn m.


Kết quả: Ghi ra thiết bị xuất chuẩn gồm một số nguyên duy nhất là độ dài nhỏ nhất của
khung hình mà các bạn học sinh cần tìm.

Vi dụ:

Sample Tnput Sample 0utput Giải thích

3 Các đoạn số nằm trọn trong khung hình 1x3
khi trượt từ trái qua phải là:
Lần 1: 35645 1. Tổng: 14.
Lần 2: 3 5 6 4 5 1. Tổng: 15.
Lần 3: 35645 1. Tổng: 15.
Lần 4: 3 5 Tổng: 19.


#### Giới hạn:

© 50% số test có n < 5000.
© 50% số test còn lại có  < 105.

### Câu 4. TÌM SO (2.0 điểm) Tên chương trình: CAU4.*

Cho số tự nhiên a, hãy tìm số tự nhiên x thỏa mãn hai điều kiện:
° x<a.
e Biểu diễn thập phân của x gồm các chữ số theo thứ tự tăng nghiêm ngặt từ trái qua
phải (từ hàng cao nhất tới hàng đơn vị). Nếu biểu diễn thập phân của x chỉ có một chữ số thì x
cũng được coi là thỏa mãn điều kiện này.
Dữ liệu: Vào từ thiết bị nhập chuẩn gồm:
© Dòng 1: Chita số nguyên dương T < 105 là số test
© T dòng tiếp theo, mỗi dòng chứa một số tự nhiên a ứng với một test (0 < a < 10)
Kết quả: Ghi ra thiết bị xuất chuẩn 7 dòng, mỗi dòng ghi kết quả là số x tìm được với test
tương ứng.

Trang 3/4

“O


#### Ví dụ:


Sample Input

Sample Output

8
9

11

1999

5678

3498
135246
345341
123456788


#### Giới hạn:


Có 10% số test còn lại không có ràn

9

9

789

5678
3489
134789
256789
23456789

Có 40% số test ứng với T < 10 và a < 10°
Có 30% số test khác ứng với a < 10°
Có 20% số test khác ứng với T < 100

g buộc gì thêm.
HET

Ghi chú

: Thi sinh không được sử dung tài liệu, cán bộ coi thi không giải thích gì thêm.

Trang 4/4