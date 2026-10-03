# Đề thi tuyển sinh 10 chuyên tin tỉnh Khánh Hòa năm 2021

- **Tỉnh/Thành phố:** Khánh Hòa
- **Trường:** THPT Chuyên Lê Quý Đôn
- **Năm học:** 2021 - 2022
- **Môn thi:** Tin học (Chuyên)

---

## NỘI DUNG ĐỀ THI

Trang 1/3
SỞ GIÁO DỤC VÀ ĐÀO TẠO
KỲ THI TUYỂN SINH VÀO LỚP 10

KHÁNH HÒA
TRƯỜNG THPT CHUYÊN LÊ QUÝ ĐÔN


Năm học 2021-2022





Môn thi: TIN HỌC

(Đề thi có 03 trang)
Ngày thi: 04/6/2021


Thời gian: 150 phút (không kể thời gian phát đề)


⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
TỔNG QUAN ĐỀ THI
TT
Tên bài
Tệp chương trình Tệp dữ liệu vào
Tệp kết quả
1
Cho kẹo
CHOKEO.*
CHOKEO.INP
CHOKEO.OUT
2
Lũy thừa của hai số
ALTB.*
ALTB.INP
ALTB.OUT
3
Số nguyên tố đặc biệt
SNTDB.*
SNTDB.INP
SNTDB.OUT
4
Dãy số lòng chảo
DAYSOLC.*
DAYSOLC.INP
DAYSOLC.OUT
(Dấu * được thay thế bởi PAS hoặc CPP của ngôn ngữ lập trình được sử dụng tương ứng là
Pascal hoặc C++)
Hãy lập trình giải các bài toán sau:

### Bài 1 (2,50 điểm): Cho kẹo

Ngày hôm nay Tí đi xem phim cùng Tèo. Như thường lệ, Tí mang theo 𝑎 gói kẹo cam
và 𝑏 gói kẹo chanh, mỗi gói đều có 𝑘 cái kẹo. Trên đường đi Tí ăn hết 𝑥 cái kẹo cam và 𝑦 cái
kẹo chanh. Lúc đến rạp chiếu phim Tí chia đôi số kẹo mỗi loại thành hai phần rồi cho Tèo
một phần sao cho độ chênh lệch số kẹo trong mỗi phần của Tí và Tèo là ít nhất. Nếu có chênh
lệch thì Tí sẽ lấy phần nhiều hơn.

#### Yêu cầu: Hãy cho biết số kẹo mỗi loại còn lại của Tí là bao nhiêu sau khi đã cho Tèo.


#### Dữ liệu vào: Từ tệp văn bản CHOKEO.INP gồm 5 số nguyên dương 𝑎, 𝑏, 𝑘, 𝑥, 𝑦 được

ghi trên một dòng và giữa các số cách nhau một dấu cách. Các số trong tệp có giá trị không
vượt quá 100.
Kết quả: Ghi vào tệp CHOKEO.OUT hai số nguyên trên một dòng theo thứ tự là số
kẹo cam và kẹo chanh của Tí sau khi đã chia cho Tèo. Giữa hai số cách nhau một dấu cách.

#### Ví dụ:

CHOKEO.INP
CHOKEO.OUT
5 3 4 10 7
5 3

ĐỀ THI CHÍNH THỨC
chuyentin.pro

Trang 2/3

### Bài 2 (3,00 điểm): Lũy thừa của hai số

Cho hai số nguyên dương 𝑛 và 𝑘. Hãy tìm hai số nguyên dương 𝑎 và 𝑏 sao cho 𝑎𝑏= 𝑛
và 𝑎+ 𝑏= 𝑘.

#### Dữ liệu vào: Từ tệp văn bản ALTB.INP gồm một dòng ghi hai số nguyên dương 𝑛 và

𝑘 ( 𝑛≤1019, 𝑘≤20) và giữa hai số được ghi cách nhau một dấu cách.
Kết quả: Ghi vào tệp văn bản ALTB.OUT hai số 𝑎 và 𝑏 tìm được trên cùng một dòng
và cách nhau một dấu cách. Nếu tìm được nhiều hơn một bộ nghiệm thì chỉ chọn một bộ
nghiệm có giá trị của 𝑎 nhỏ nhất. Nếu không tìm được hai số 𝑎 và 𝑏 thỏa điều kiện bài toán
thì ghi số -1.

#### Ví dụ:

ALTB.INP
ALTB.OUT
16 6
2 4

### Bài 3 (2,50 điểm): Số nguyên tố đặc biệt

Hải là người yêu thích các số nguyên tố chính vì vậy cậu ta thường tìm ra những số
nguyên tố có tính chất đặc biệt. Hải đã phát hiện ra có những số nguyên tố mà tổng các chữ
số của nó cũng là số nguyên tố. Ví dụ: số 67 có tổng hai chữ số của nó bằng 13 cũng là một
số nguyên tố. Hải gọi những số nguyên tố như vậy là số nguyên tố đặc biệt.

#### Yêu cầu: Cho hai số nguyên 𝑙, 𝑟 hãy cho biết trong đoạn từ 𝑙 đến 𝑟 có những số nguyên

tố đặc biệt nào?

#### Dữ liệu vào: Từ tệp SNTDB.INP gồm hai số nguyên dương 𝑙, 𝑟 (1 ≤𝑙≤𝑟≤107)

trên một dòng và cách nhau một dấu cách. Dữ liệu vào luôn đảm bảo có bài toán có nghiệm.
Kết quả: Ghi vào tệp SNTDB.OUT các số nguyên tố đặc biệt từ 𝑙 đến 𝑟. Các số in ra
theo thứ tự tăng dần và cách nhau một dấu cách.

#### Ví dụ:

SNTDB.INP
SNTDB.OUT
10 50
11 23 29 41 43 47

### Bài 4 (2,00 điểm): Dãy số lòng chảo

Người ta gọi một dãy số có tính chất lòng chảo là dãy số mà nếu các số trong dãy có
giá trị giảm dần tính từ đầu dãy hướng về phía giữa dãy rồi sau đó lại tăng dần về phía cuối
dãy. Ví dụ: Dãy số {3, 2, 1, 3, 4, 5} được xem là dãy số lòng chảo.  Các dãy số {4, 2, 2, 3};
{3, 2, 1} và {1, 2, 3, 2, 1} không được xem là dãy số lòng chảo.
chuyentin.pro

Trang 3/3

#### Yêu cầu: Cho một dãy số gồm 𝑛 số nguyên  𝐴1, 𝐴2, … , 𝐴𝑛. Hãy tìm một dãy con (có ít

nhất ba số) gồm các số liên tiếp nhau trong dãy số đã cho là dãy số lòng chảo và có độ dài lớn
nhất.

#### Dữ liệu vào: Tệp văn bản DAYSOLC.INP gồm:

+ Dòng đầu ghi số nguyên dương  𝑛 (𝑛≤103).
+ Dòng thứ hai ghi 𝑛 số nguyên trong dãy 𝐴1, 𝐴2, … , 𝐴𝑛 (0 ≤𝐴𝑖≤105, 𝑖= 1 … 𝑛).
Giữa các số cách nhau một dấu cách.
Kết quả: Ghi vào tệp văn bản DAYSOLC.OUT dãy số đầu tiên tìm được thỏa yêu
cầu bài toán. Nếu không tìm được dãy số thỏa điều kiện bài toán thì ghi số -1.

#### Ví dụ 1:

DAYSOLC.INP
DAYSOLC.OUT
8
3 2 1 3 4 5 1 2
3 2 1 3 4 5

#### Ví dụ 2:

DAYSOLC.INP
DAYSOLC.OUT
4
4 2 2 3
-1
⎯⎯⎯⎯⎯⎯⎯⎯  HẾT ⎯⎯⎯⎯⎯⎯⎯⎯
Lưu ý:
+ Thí sinh không sử dụng lệnh tạm dừng ở cuối chương trình (ví dụ: lệnh readln trong
PASCAL).
+ Thời gian chạy chương trình của mỗi bài cho mỗi test không vượt quá 01 giây.
- Giám thị không giải thích gì thêm.
- Họ và tên thí sinh:……………………………………………SBD:……………/Phòng:………….
- Giám thị 1:………………….………….……Giám thị 2: …..………………………………………
chuyentin.pro