# Đề thi tuyển sinh 10 chuyên tin tỉnh Khánh Hòa năm 2020

- **Tỉnh/Thành phố:** Khánh Hòa
- **Trường:** THPT Chuyên Lê Quý Đôn
- **Năm học:** 2020 - 2021
- **Môn thi:** Tin học (Chuyên)

---

## NỘI DUNG ĐỀ THI

Trang 1/3
SỞ GIÁO DỤC VÀ ĐÀO TẠO
KỲ THI TUYỂN SINH VÀO LỚP 10

KHÁNH HÒA
TRƯỜNG THPT CHUYÊN LÊ QUÝ ĐÔN

⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
Năm học 2020-2021


⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯


Môn thi: TIN HỌC

(Đề thi có 03 trang)
Ngày thi: 07/7/2020


(Thời gian: 150 phút, không kể thời gian phát đề)


⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
TỔNG QUAN ĐỀ THI
STT
Tên bài
Tệp chương trình

#### Dữ liệu vào

Kết quả
1
Trang trí hàng cây
TRANGTRI.*
TRANGTRI.INP TRANGTRI.OUT
2
Chi phiếu
INSEC.*
INSEC.INP
INSEC.OUT
3
Số lân cận
LANCAN.*
TAMGIAC.INP
LANCAN.OUT
4
Dán nhãn
DANNHAN.*
DANNHAN.INP DANNHAN.OUT
(Dấu * được thay thế bởi PAS hoặc CPP của ngôn ngữ lập trình được sử dụng tương
ứng là Pascal hoặc C++)
Hãy lập trình giải các bài toán sau:

### Bài 1. (2,0 điểm): Trang trí hàng cây

Dọc theo một con đường thẳng người ta trồng một hàng gồm 𝑛 cây xanh có khoảng cách
đều nhau. Để trang trí cho con đường vào ban đêm, người ta gắn lên hàng cây một số bóng
đèn theo quy tắc xen kẽ, cứ hai cây liền kề nhau thì một cây được gắn đèn, một cây không
gắn đèn. Biết rằng để gắn một bóng đèn lên một cây thì cần chi phí với số tiền là 𝑥 đồng.

#### Yêu cầu: Hãy tính tổng chi phí để gắn được nhiều bóng đèn nhất cho hàng cây.


#### Dữ liệu vào: Từ tệp văn bản TRANGTRI.INP chỉ gồm một dòng ghi hai số nguyên 𝑛

và 𝑥 cách nhau một dấu cách.

#### Giới hạn:

+ 1 ≤𝑛≤109
+ 1 ≤𝑥≤103
Kết quả: Ghi ra tệp văn bản TRANGTRI.OUT một số nguyên là kết quả tìm được của
bài toán.
TRANGTRI.INP
TRANGTRI.OUT
5 10
30

### Bài 2. (3,0 điểm): Chi phiếu

Tí là tổng giám đốc một công ty lớn có rất nhiều đối tác làm ăn. Hôm nay một đối tác

#### yêu cầu Tí phải chuyển cho họ một số tiền 𝑑 qua chi phiếu. Trợ lý bảo rằng bàn phím máy

tính in chi phiếu đã hỏng mất phím số 4 nên không thể in được số tiền trong chi phiếu vì giá
trị của số tiền có chữ số 4.
ĐỀ THI CHÍNH THỨC
chuyentin.pro

Trang 2/3
Tí là người thông minh nên đã gợi ý cho trợ lý khắc phục bằng cách in thành hai tờ sao
cho tổng số tiền ghi trên hai tờ cộng lại đúng bằng 𝑑 và giá trị tiền trên hai tờ lệch nhau ít nhất
có thể.

#### Yêu cầu: Hãy giúp trợ lý tính số tờ tiền cần in trên hai tờ chi phiếu theo yêu cầu của Tí.


#### Dữ liệu vào: Từ tệp văn bản INSEC.INP chỉ ghi số nguyên dương 𝑑.

Gới hạn: 𝑑≤106
Kết quả: Ghi ra tệp văn bản INSEC.OUT hai số nguyên tìm được thỏa mãn yêu cầu bài
toán, số nhỏ hơn in trước số lớn hơn in sau và giữa chúng cách nhau một dấu cách.

#### Ví dụ:

INSEC.INP
INSEC.OUT
489
239 250

### Bài 3. (2,5 điểm): Số lân cận

Độ lân cận của một số 𝑥 với một số 𝑦 được tính bằng công thức: 𝑑(𝑥, 𝑦) = |𝑥−𝑦|. Độ
lân cận của một số với dãy số là độ lân cận nhỏ nhất của số đó với các số khác trong dãy. Ví
dụ, dãy gồm 4 số {3,8,2,10} thì độ lân cận của số 3 với ba số trong dãy {8,2,10} là 𝑑(3,8) =
5; 𝑑(3,2) = 1; 𝑑(3,10) = 7. Do vậy độ lân cận của 3 với dãy số đã cho là 1.
Cho một dãy gồm 𝑛 số nguyên  𝑎1, 𝑎2, … , 𝑎𝑛.

#### Yêu cầu: Hãy tính tổng độ lân cận của các số trong dãy số


#### Dữ liệu vào: Từ tệp văn bản LANCAN.INP gồm:

+ Dòng đầu tiên ghi số nguyên 𝑛 là số lượng các số trong dãy.
+ Dòng thứ hai ghi 𝑛 số nguyên 𝑎1, 𝑎2, … , 𝑎𝑛
Gới hạn:
+ 3 ≤𝑛≤105
+ 1 ≤𝑎𝑖≤106 (𝑖= 1 … 𝑛)
Kết quả: Ghi ra tệp văn bản LANCAN.OUT một số nguyên duy nhất là tổng độ lân cận
của các số trong dãy.

#### Ví dụ:

LANCAN.INP
LANCAN.OUT
4
3 8 2 10
6
Giải thích ví dụ:
+ Độ lân cận của 3 với dãy {8,2,10} = 1
+ Độ lân cận của 8 với dãy {3,2,10} = 2
+ Độ lân cận của 2 với dãy {3,8,10} = 1
+ Độ lân cận của 10 với dãy {3,8,2} = 2
Như vậy tổng độ lân cận của các số trong dãy số đã cho là 1 + 2 + 1 + 2 = 6

### Bài 4. (2,5 điểm): Dán nhãn

Một dây chuyền sản xuất thiết bị vừa sản xuất được 𝑛 sản phẩm và đã dán nhãn cho mỗi
sản phẩm một mã số để tiện quản lý. Mã số được dán cho mỗi sản phầm là một số nguyên
dương và không không được có hai sản phẩm bất kỳ nào có mã số trùng nhau. Không may là
chuyentin.pro

Trang 3/3
dây chuyền dán nhãn bị lỗi nên trong những sản phẩm đã dán nhãn có thể có nhiều sản phẩm
được dán cùng một nhãn (có mã số giống nhau).

#### Yêu cầu: Hãy tìm xem trong 𝑛 sản phẩm đã dán nhãn có ít nhất bao nhiêu sản phẩm cần

dán lại để tất cả các sản phẩm đều có mã số khác nhau.

#### Dữ liệu vào: Từ tệp văn bản DANNHAN.INP gồm:

+ Dòng đầu tiên ghi số nguyên dương 𝑛.
+ Dòng thứ hai ghi 𝑛 số nguyên dương được cách nhau một dấu cách là nhãn của 𝑛 sản
phẩm đã được dán

#### Giới hạn:

+ 1 ≤𝑛≤106
+ Nhãn của 𝑛 sản phẩm là các số nguyên dương có giá trị không vượt quá 107
Kết quả: ghi ra tệp DANNHAN.OUT một số nguyên cho biết số lượng ít nhất sản phẩm
cần phải dán lại nhãn

#### Ví dụ:

DANNHAN.INP
DANNHAN.OUT
7
1 2 2 4 2 5 1
3
Giải thích: Trong ví dụ trên cần dán lại một nhãn có mã số 1 và 2 nhãn có mã số 2, do
vậy số lượng ít nhất sản phẩm cần dán nhãn lại là 3.
⎯⎯⎯⎯⎯⎯⎯⎯  HẾT ⎯⎯⎯⎯⎯⎯⎯⎯
Lưu ý:
+ Thí sinh không sử dụng lệnh tạm dừng ở cuối chương trình (ví dụ: lệnh readln trong
PASCAL).
+ Thời gian chạy chương trình của mỗi bài cho mỗi test không vượt quá 01 giây.
- Giám thị không giải thích gì thêm.
- Họ và tên thí sinh:……………………………………………SBD:……………/Phòng:………….
- Giám thị 1:………………….………….……Giám thị 2: …..………………………………………
chuyentin.pro