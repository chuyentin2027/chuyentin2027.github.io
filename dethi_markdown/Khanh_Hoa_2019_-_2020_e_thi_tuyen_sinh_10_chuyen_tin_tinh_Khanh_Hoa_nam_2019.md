# Đề thi tuyển sinh 10 chuyên tin tỉnh Khánh Hòa năm 2019

- **Tỉnh/Thành phố:** Khánh Hòa
- **Trường:** THPT Chuyên Lê Quý Đôn
- **Năm học:** 2019 - 2020
- **Môn thi:** Tin học (Chuyên)

---

## NỘI DUNG ĐỀ THI

Trang 1/3
SỞ GIÁO DỤC VÀ ĐÀO TẠO
KỲ THI TUYỂN SINH VÀO LỚP 10

KHÁNH HÒA
TRƯỜNG THPT CHUYÊN LÊ QUÝ ĐÔN

⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
Năm học 2019-2020


⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯


Môn thi: TIN HỌC

(Đề thi có 03 trang)
Ngày thi: 05/6/2019


(Thời gian: 150 phút, không kể thời gian phát đề)


⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
TỔNG QUAN ĐỀ THI
STT
Tên bài
Tệp chương trình

#### Dữ liệu vào

Kết quả
1
Lát gạch
LATGACH.*
Nhập từ bàn phím In ra màn hình
2
Alibaba
ALIBABA.*
Nhập từ bàn phím In ra màn hình
3
Tam giác
TAMGIAC.*
TAMGIAC.INP
TAMGIAC.OUT
4
Xếp táo
XEPTAO.*
XEPTAO.INP
XEPTAO.OUT
(Dấu * được thay thế bởi PAS hoặc CPP của ngôn ngữ lập trình được sử dụng tương
ứng là Pascal hoặc C++)
Hãy lập trình giải các bài toán sau:

### Bài 1. (6,0 điểm) – LÁT GẠCH

Một cái sân hình chữ nhật có chiều ngang là n dm và chiều dọc là d dm. Người ta cần
lát mặt sân bằng một loại gạch hình chữ nhật có chiều rộng là 1 dm và chiều dài là 2 dm.
Mỗi viên gạch có thể được lát ngang hoặc lát dọc tùy ý, miễn sao gạch phải phủ vừa đủ diện
tích của sân. Trong một số trường hợp, người ta phải cắt đôi viên gạch thành hai nửa viên
hình vuông dùng để lát ô có diện tích bằng 1×1.

#### Yêu cầu: Bạn hãy lập trình tính số viên gạch ít nhất cần phải cắt để lát đủ mặt sân.


#### Dữ liệu vào: Nhập từ bàn phím hai số nguyên n và d (0 < n, d ≤ 103) theo đúng thứ tự.

Kết quả: In ra màn hình một số nguyên là số lượng viên gạch ít nhất cần phải cắt.

#### Ví dụ:

Nhập từ bàn phím
In ra màn hình
3 3
1

### Bài 2. (5,0 điểm) – ALIBABA

Alibaba nói rằng: anh ấy có n đồng tiền gồm ba loại là vàng, bạc và đồng, trong đó số
đồng tiền vàng ít hơn số đồng tiền bạc là d và số đồng tiền bạc cũng ít hơn số đồng tiền
đồng là d.
ĐỀ THI CHÍNH THỨC
chuyentin.pro

Trang 2/3

#### Yêu cầu: Bạn hãy lập trình xác định xem Alibaba nói có đúng không? Nếu anh ấy nói

đúng thì anh ấy đang có bao nhiêu đồng tiền vàng, bạc và đồng?

#### Dữ liệu vào: Nhập từ bàn phím hai số nguyên dương n và d (0 < d < n  ≤109) theo

đúng thứ tự.
Kết quả: In ra màn hình ba số nguyên tương ứng là số đồng tiền vàng, bạc và đồng mà
Alibaba đang có. Giữa các số cách nhau đúng một dấu cách. Nếu bài toán không có lời giải
(Alibaba nói sai) thì chỉ in ra số -1.

#### Ví dụ:

Nhập từ bàn phím
In ra màn hình
12 2
2 4 6

Nhập từ bàn phím
In ra màn hình
20 3
-1

### Bài 3. (5,0 điểm) – TAM GIÁC

Cho một dãy gồm n số nguyên dương A1, A2,…, An. Hãy chọn ra ba số trong dãy (mỗi
số chỉ được chọn một lần) sao cho ba số được chọn là số đo độ dài tương ứng của ba cạnh
tam giác có chu vi lớn nhất.

#### Dữ liệu vào: Từ tệp văn bản TAMGIAC.INP gồm:

- Dòng đầu ghi số nguyên dương n (3 ≤ n ≤ 105);
- Dòng thứ hai ghi n số nguyên dương A1, A2, …, An. Mỗi số có giá trị không vượt quá
109 và giữa chúng cách nhau đúng một dấu cách.
Kết quả: Ghi ra tệp văn bản TAMGIAC.OUT ba số nguyên thỏa mãn điều kiện bài
toán theo thứ tự từ lớn đến nhỏ và giữa các số phải cách nhau đúng một dấu cách. Nếu
không tìm được ba số thỏa mãn điều kiện bài toán thì ghi số -1.

#### Ví dụ:

TAMGIAC.INP
TAMGIAC.OUT
4
3 5 1 4
5 4 3

TAMGIAC.INP
TAMGIAC.OUT
4
2 9 2 15
-1

chuyentin.pro

Trang 3/3

### Bài 4. (4,0 điểm) – XẾP TÁO

Siêu thị Big.C Nha Trang đang bày bán rất nhiều loại hoa quả, trong đó có n quả cam
và n quả táo được xếp thành một dãy rất dài. Trong quá trình xếp, các nhân viên đã vô ý xếp
những quả cam và những quả táo không theo một thứ tự nhất định. Quản lý siêu thị yêu cầu
các nhân viên phải xếp lại sao cho chúng được xếp xen kẻ nhau, cứ một quả cam rồi lại đến
một quả táo và ngược lại.
Các hành động lấy một quả cam hoặc quả táo ra khỏi dãy, dồn những quả bên trái hoặc
bên phải về chỗ trống vừa lấy và chèn quả vừa lấy vào vị trí thích hợp được xem là một thao
tác.

#### Yêu cầu: Bạn hãy giúp người quản lý siêu thị tính xem cần ít nhất bao nhiêu thao tác

để xếp lại dãy quả cam và quả táo.

#### Dữ liệu vào: Từ tệp văn bản XEPTAO.INP gồm:

- Dòng đầu ghi số nguyên dương n (n ≤ 106).
- Dòng thứ hai ghi 2.n ký tự ‘0’ và ‘1’, trong đó những ký tự ‘0’ biểu thị cho vị trí các
quả cam còn những ký tự ‘1’ biểu thị cho vị trí các quả táo.
Kết quả: Ghi ra tệp văn bản XEPTAO.OUT một số nguyên duy nhất là số thao tác ít
nhất cần thực hiện để xếp lại dãy quả cam và quả táo theo đúng yêu cầu bài toán.

#### Ví dụ:

XEPTAO.INP
XEPTAO.OUT
3
100011
2

⎯⎯⎯⎯⎯⎯⎯⎯  HẾT ⎯⎯⎯⎯⎯⎯⎯⎯
Lưu ý:
+ Thí sinh không sử dụng lệnh tạm dừng ở cuối chương trình (ví dụ: lệnh readln trong
PASCAL).
+ Thời gian chạy chương trình của mỗi bài cho mỗi test không vượt quá 01 giây.
- Giám thị không giải thích gì thêm.
- Họ và tên thí sinh:……………………………………………SBD:……………/Phòng:………….
- Giám thị 1:………………….………….……Giám thị 2: …..………………………………………
chuyentin.pro