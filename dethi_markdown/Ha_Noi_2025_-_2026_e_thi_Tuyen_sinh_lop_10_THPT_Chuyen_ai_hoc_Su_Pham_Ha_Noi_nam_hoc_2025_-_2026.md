# Đề thi Tuyển sinh lớp 10 THPT Chuyên Đại học Sư Phạm Hà Nội năm học 2025 - 2026

- **Tỉnh/Thành phố:** Hà Nội
- **Trường:** THPT Chuyên Đại học Sư phạm Hà Nội
- **Năm học:** 2025 - 2026
- **Môn thi:** Tin học (Chuyên)

---

## NỘI DUNG ĐỀ THI

1
1. 25-26 TS10 HANOI DHSP
Link đề gốc:
ĐỀ THI TUYỂN SINH VÀO LỚP 10 CHUYÊN TIN
TRƯỜNG ĐẠI HỌC SƯ PHẠM HÀ NỘI, NĂM HỌC 2025 – 2026
Thời gian làm bài: … phút, ngày thi …/06/2025
TỔNG QUAN ĐỀ THI
Bài
Tên bài
Tên file CT
File input
File output
Điểm
1
Ước nguyên tố
UOCNT.*
UOCNT.INP
UOCNT.OUT

2
Chạy tiếp sức
TIEPSUC.*
TIEPSUC.INP
TIEPSUC.OUT

3
Những gói kẹo
GOIKEO.*
GOIKEO.INP
GOIKEO.OUT

4
Lời chào
LOICHAO.*
LOICHAO.INP
LOICHAO.OUT

Dấu * được thay thế bởi PAS, CPP hoặc PY tương ứng với ngôn ngữ lập trình sử dụng
LẬP TRÌNH GIẢI CÁC BÀI TOÁN SAU


### Câu 1.

UOCNT Ước nguyên tố
Với một số nguyên dương x ≥ 2, gọi f (x) là ước số nguyên tố lớn nhất của x.

#### Yêu cầu: Cho số n và q câu hỏi, mỗi câu hỏi cho bởi số nguyên dương k. Bạn hãy cho biết trong

phạm vi từ 2 tới n có bao nhiêu giá trị x mà f(x) ≤ k.

#### Input:

• Dòng 1 chứa hai số nguyên dương n, q cách nhau bởi dấu cách (2 ≤ n ≤ 106; q ≤ 106)
• q dòng tiếp theo, mỗi dòng chứa một số nguyên dương k ứng với một câu hỏi (2 ≤ k ≤ n)

#### Output: Ghi ra thiết bị xuất chuẩn q dòng, ứng với mỗi câu hỏi, ghi ra một số nguyên trên một dòng

là đáp số của câu hỏi tương ứng.

#### Ví dụ


#### Input


#### Output

Giải thích
10 4
2
5
3
8
3
8
6
9
Từ 2 tới 10 có:
3 số x có f(x) ≤ 2: 2, 4, 8
8 số x có f(x) ≤ 5: 2, 3, 4, 5, 6, 8, 9, 10
6 số x có f(x) ≤ 3: 2, 3, 4, 6, 8, 9
9 số x có f(x) ≤ 8: 2, 3, 4, 5, 6, 7, 8, 9, 10

#### Giới hạn

• 60% số test có n ≤ 104; q ≤ 10
• 40% số test không có ràng buộc bổ sung.

### Câu 2.

TIEPSUC Chạy tiếp sức

Ba vận động viên A, B, C thuộc cùng một đội tham gia giải chạy tiếp sức. Đường đua được
chia làm n chặng đánh số từ 1 tới n dọc chiều dài đường đua, chặng thứ i có độ dài ai mét.

Căn cứ vào thực lực của các vận động viên, huấn luyện viên của đội đề ra chiến thuật chạy
thỏa mãn ba yêu cầu sau: đây.
• A sẽ chạy những chặng đầu tiên, tiếp theo là B chạy những chặng kế tiếp, kết thúc là C chạy
những chặng cuối cùng

2
• Mỗi vận động viên phải chạy nguyên một số (có thể bằng 0) chặng liên tiếp
• Quãng đường chạy của A ngắn hơn hoặc bằng quãng đường chạy của B, quãng đường chạy
của B ngắn hơn hoặc bằng quãng đường chạy của C

#### Yêu cầu: Dù A là vận động viên yếu nhất và phải chạy quãng đường ngắn nhất nhưng huấn luyện

viên cũng muốn A coi cuộc đua là một cơ hội luyện tập. Vì vậy huấn luyện viên muốn nhờ bạn phân
chia chặng đường chạy cho ba vận động viên thỏa mãn cả ba yêu cầu trên mà độ dài quãng đường
chạy của A là lớn nhất có thể.

#### Input:

• Dòng 1 chứa số nguyên dương n (3 ≤ n ≤ 106)
• Dòng 2 chứa n số nguyên dương a1, a2, ..., an, cách nhau bởi dấu cách (ai ≤ 106)

#### Output: Ghi một số nguyên duy nhất là độ dài quãng đường chạy của A theo phương án tìm được.


#### Ví dụ:


#### Input


#### Output

Giải thích
6
1000 2000 3000 1000 4000 2000

3000

A chạy 2 chặng đầu: 1000 + 2000 = 3000
B chạy 2 chặng tiếp: 3000 + 1000 = 4000
C chạy 2 chặng cuối: 4000 + 2000 = 6000
8
100 1 2 3 4 5 6 7
0

A và B không chạy chặng nào C chạy hết
cả đường đua
9
4 2 1 4 1 9 3 3 3
6

A chạy 2 chặng đầu: 4 + 2 = 6
B chạy 3 chặng tiếp: 1 + 4 + 1
C chạy 4 chặng cuối: 9 + 3 + 3 + 3 = 18
11
9 3 1 8 7 1 3 1 1 7 2
13


#### Giới hạn:

• 30% số test có n ≤ 100
• 40% số test có n ≤ 5000
• 30% số test không có ràng buộc bổ sung.

### Câu 3.

GOIKEO Những gói kẹo

Nhân ngày 1/6, giáo sư X mang tới n gói kẹo để làm quà cho các bé thiếu nhi trường mầm non
SuperKids. Các gói kẹo được đánh số từ 1 tới n, gói thứ i có ai viên kẹo. Tuy nhiên khi đến trường
giáo sư mới biết được số các bé thiếu nhi là m (m < n) vì vậy ông cần phân phối lại để có được m gói
có số kẹo bằng nhau để phát cho các bé.

#### Yêu cầu: Biết rằng trong mỗi giây giáo sư X có thể lấy đúng một viên kẹo từ một gói chuyển sang

một gói khác. Hãy cho biết thời gian tối thiểu giáo sư X cần để thu được m gói kẹo với số kẹo bằng
nhau từ n gói kẹo ban đầu.

#### Input

• Dòng 1 chứa hai số nguyên dương n, m (1 ≤ m < n ≤ 106)
• Dòng 2 chứa n số nguyên dương a1, a2, ..., an (ai ≤ 109)
Các số trên một dòng của input được ghi cách nhau bởi dấu cách

#### Output: Ghi một số nguyên duy nhất là số giây tối thiểu giáo sư X cần để thu được m gói kẹo với số

kẹo bằng nhau từ n gói kẹo ban đầu.

3

#### Ví dụ:


#### Input


#### Output

Giải thích
4 3
6 3 8 9

2

Chuyển 1 viên từ gói 2 sang gói 1
Chuyển 1 viên từ gói 4 sang gói 1
Thu được: 8 2 8 8
6 4
3 8 9 4 3 3

1

Chuyển 1 viên từ gói 4 sang gói 2
Thu được: 3 9 9 3 3 3
7 5
1 1 2 5 5 5 5

4

Chuyển 1 viên từ gói 4 sang gói 1
Chuyển 1 viên từ gói 5 sang gói 1
Chuyển 1 viên từ gói 6 sang gói 3
Chuyển 1 viên từ gói 7 sang gói 3
Thu được: 3 1 4 4 4 4 4

#### Giới hạn:

• 40% số test có n ≤ 1000 và a1, a2, …, an ≤ 1000
• 30% số test có n ≤ 1000
• 30% số test không có ràng buộc bổ sung.

### Câu 4.

LOICHAO Lời chào

Có n chú kiến đánh số từ 1 tới n đứng quanh một cái hồ hình tròn có chu vi n mét. Theo chiều
kim đồng hồ, sau 1 mét từ chú kiến 1 là chú kiến 2, sau 1 mét từ chú kiến 2 là chú kiến 3, ..., sau 1
mét từ chú kiến n là chú kiến 1. Các chú kiến xuất phát cùng lúc, di chuyển quanh hồ với tốc độ như
nhau. Với mỗi chú kiến i, ta được biết hai thông tin:
• Ký tự ci, cho biết hướng đi: ci =' +’ nếu chú kiến thứ i đi theo chiều kim đồng hồ, ci = ' - '
nếu chú kiến thứ i đi ngược chiều kim đồng hồ.
• Số nguyên dương di cho biết độ dài quãng đường mà chú kiến thứ i sẽ đi

Nếu hai chú kiến đi ngược chiều gặp nhau, chúng sẽ chạm râu để thực hiện lời chào rồi đi tiếp.
Thời gian chào không đáng kể và không ảnh hưởng tới tốc độ cũng như hướng đi của kiến. Lưu ý
rằng hai chú kiến có thể gặp và chào nhau nhiều lần. Sau khi chú kiến đi hết quãng đường đã định, nó
sẽ rời khỏi vòng hồ và không thực hiện bất kỳ lời chào nào nữa.

#### Yêu cầu: Với mỗi chú kiến, hãy cho biết trong suốt hành trình đã có bao nhiêu lời chào được chú

kiến đó thực hiện (lời chào thực hiện vào đúng thời điểm một trong hai chú kiến kết thúc hành trình
cũng được tính nếu có)

#### Input:

• Dòng 1 chứa số nguyên dương n (n ≤ 2 × 105)
• n dòng tiếp theo, mỗi dòng chứa ký tự ci, và số nguyên dương di liền nhau (di ≤ 109)

#### Output: Ghi n dòng, dòng thứ i ghi một số nguyên là số lời chào mà chú kiến i thực hiện trong suốt

hành trình của mình.

4

#### Ví dụ


#### Input


#### Output

Giải thích
Minh họa
6
+4
-5
-5
+5
+5
-3
5
6
5
4
5
3

Kiến 1 chào lần lượt: 2, 3, 6, 2, 3
Kiến 2 chào lần lượt: 1, 5, 4, 1, 5, 4
Kiến 3 chào lần lượt: 1, 5, 4, 1, 5
Kiến 4 chào lần lượt: 6, 2, 3, 2
Kiến 5 chào lần lượt: 6, 2, 3, 2, 3
Kiến 6 chào lần lượt: 5, 4, 1


#### Giới hạn:

• 30% số test có n, d1, d2, ..., dn ≤ 100
• 30% số test có n ≤ 5000
• 20% số test có d1 = d2 = … = dn
• 20% số test không có ràng buộc bổ sung.