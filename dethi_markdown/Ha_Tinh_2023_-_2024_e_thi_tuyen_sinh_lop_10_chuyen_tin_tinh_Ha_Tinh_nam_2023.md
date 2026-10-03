# Đề thi tuyển sinh lớp 10 chuyên tin tỉnh Hà Tĩnh năm 2023

- **Tỉnh/Thành phố:** Hà Tĩnh
- **Trường:** THPT Chuyên Hà Tĩnh
- **Năm học:** 2023 - 2024
- **Môn thi:** Tin học (Chuyên)

---

## NỘI DUNG ĐỀ THI

Trang 1/3

SỞ GIÁO DỤC VÀ ĐÀO TẠO
HÀ TĨNH
KỲ THI TUYỂN SINH VÀO LỚP 10 THPT
TRƯỜNG THPT CHUYÊN HÀ TĨNH

NĂM HỌC 2023-2024
Môn: TIN HỌC
(Đề thi có 03 trang, gồm 04 bài)
Thời gian làm bài: 150 phút, không kể thời gian phát đề
TỔNG QUAN BÀI THI

Tên bài
File chương trình
File dữ liệu
File kết quả

### Bài 1

Tổng dãy số
SUMS.*
SUMS.INP
SUMS.OUT

### Bài 2

Số đặc biệt
BNUM.*
BNUM.INP
BNUM.OUT

### Bài 3

Dãy đặc trưng
SPEC.*
SPEC.INP
SPEC.OUT

### Bài 4

Đoạn thẳng
PPOINT.*
PPOINT.INP
PPOINT.OUT
Dấu * được thay thế bởi PAS hoặc CPP hoặc PY tương ứng với ngôn ngữ lập trình Pascal hoặc
C++ hoặc Python.
Hãy lập trình giải các bài toán sau:

### Bài 1. Tổng dãy số (3,0 điểm)

Cho dãy số T1, T2, T3, …, Tn.
Với số hạng tổng quát là: Tk = (k+1)2 – k2 (k là số nguyên và 1     ).

#### Yêu cầu: Tính giá trị S = T1 + T2 + T3 + … + Tn

Dữ liệu
Vào từ file văn bản SUMS.INP gồm một dòng duy nhất chứa số nguyên dương n (1     109).
Kết quả
Ghi ra file văn bản SUMS.OUT một số nguyên là giá trị S tính được.

#### Ví dụ

SUMS.INP
SUMS.OUT
Giải thích
2
8
Với n = 2 ta có:
S = T1 + T2 = (1+1)2 – 12 +
(2+1)2 – 22 = 8

#### Ràng buộc

 Có 70% số test ứng với 70% số điểm thỏa mãn 1       .
 Có 30% số test còn lại ứng với 30% số điểm không có ràng buộc gì thêm.

### Bài 2. Số đặc biệt (3,0 điểm)

Khi tìm hiểu về số tự nhiên, Nam phát hiện ra số tự nhiên có rất nhiều tính chất thú vị. Nhiều số tự
nhiên có tính chất: Tổng bình phương các chữ số của nó là số nguyên tố, những số như thế Nam gọi
là số đặc biệt. Ví dụ số 12, 14, 21 là các số đặc biệt.
ĐỀ THI CHÍNH THỨC
chuyentin.pro

Trang 2/3


#### Yêu cầu: Cho số nguyên dương n. Hãy giúp Nam kiểm tra xem n có phải là số đặc biệt hay không.

Dữ liệu
Vào từ file văn bản BNUM.INP gồm một dòng duy nhất chứa số nguyên dương n (10        ).
Kết quả
Ghi ra file văn bản BNUM.OUT gồm 2 dòng:
 Dòng đầu ghi ra 1 nếu n là số đặc biệt, ngược lại ghi -1 nếu n không phải là số đặc biệt.
 Dòng thứ hai ghi một số là tổng bình phương các chữ số của n.

#### Ví dụ

BNUM.INP
BNUM.OUT
Giải thích
21
1
5
Số 21 là số đặc biệt vì tổng bình phương các chữ số của 21
là 22 + 12 = 5 (5 là số nguyên tố)
24
-1
20
Số 24 không phải là số đặc biệt vì tổng bình phương các chữ
số của số 24 là 22 + 42 = 20 (20 không phải số nguyên tố).

#### Ràng buộc

 Có 60% số test ứng với 60% số điểm thỏa mãn: 10       .
 40% số test còn lại ứng với 40% số điểm không có ràng buộc gì thêm.

### Bài 3. Dãy đặc trưng (2,0 điểm)

Cho một dãy A gồm n số nguyên a1, a2, …, an, mỗi phần tử có giá trị tuyệt đối không quá 109. Dãy
đặc trưng A1 của A là dãy con gồm các phần tử liên tiếp nhau thỏa mãn các yêu cầu sau:
- Trong dãy A1 tất cả các số đều dương hoặc đều âm.
- Số lượng phần tử của dãy A1 là lớn nhất.

#### Yêu cầu: Hãy tìm dãy A1 và ghi ra số lượng phần tử của nó.

Dữ liệu
Vào từ file văn bản SPEC.INP gồm 2 dòng:
 Dòng đầu chứa số nguyên dương n (n     ).
 Dòng thứ hai chứa n số a1, a2, …, an.
Các số trên cùng một dòng cách nhau một dấu cách.
Kết quả
Ghi ra file văn bản SPEC.OUT một số là số lượng các phần tử của dãy A1 tìm được.

#### Ví dụ

SPEC.INP
SPEC.OUT
Giải thích
9
1 -3 -2 1 3 1 5 -3 -4
4
Dãy A1 là: 1 3 1 5. Dãy có 4 phần tử.
7
8 -1 -2 -3 -5 -6 4
5
Dãy A1 là: -1 -2 -3 -5 -6. Dãy có 5 phần tử.
chuyentin.pro

Trang 3/3


#### Ràng buộc

 Có 60% số test ứng với 60% số điểm thỏa mãn: n     .
 40% số test còn lại ứng với 40% số điểm không có ràng buộc gì thêm.

### Bài 4. Đoạn thẳng (2,0 điểm)

Trên trục Ox cho n điểm đánh số từ 1 đến n, điểm thứ i ở vị trí tọa độ là xi (1     ). Mỗi điểm
được tô một trong 3 màu xanh, đỏ, vàng. Hãy tìm trên trục số một đoạn thẳng thỏa mãn hai điều kiện
sau:
- Trong đoạn thẳng đó mỗi màu xuất hiện ít nhất một lần.
- Độ dài đoạn thẳng là nhỏ nhất.
Dữ liệu
Vào từ file văn bản PPOINT.INP:
 Dòng đầu chứa số nguyên dương n  (1       ).
 n dòng tiếp theo, mỗi dòng chứa hai giá trị xi, mi:
+ Số nguyên xi là tọa độ của điểm thứ i trên trục số (1        , 1     ).
+ Số nguyên mi là ký hiệu màu của các điểm, trong đó mi = 1 là màu xanh, mi = 2 là màu đỏ,
mi = 3 là màu vàng.
Các số trên cùng một dòng cách nhau một dấu cách.
Kết quả
Ghi ra file văn bản PPOINT.OUT một số là độ dài đoạn thẳng thỏa mãn yêu cầu của bài toán, nếu
không tìm thấy đoạn nào thỏa mãn yêu cầu thì ghi giá trị -1.

#### Ví dụ

PPOINT.INP
PPOINT.OUT
Giải thích
6
2 1
4 1
5 2
7 2
8 3
10 3
4
Đoạn thẳng từ điểm có tọa độ 4 đến điểm có tọa
độ 8 có độ dài là 8 – 4 = 4 gồm có 1 điểm màu
xanh, 2 điểm màu đỏ và 1 điểm màu vàng.

#### Ràng buộc

 Có 30% số test ứng với 30% số điểm thỏa mãn: 1       .
 30% số test khác ứng với 30% số điểm thỏa mãn: n     .
 40% số test còn lại ứng với 40% số điểm không có ràng buộc gì thêm.

--------------HẾT--------------
chuyentin.pro