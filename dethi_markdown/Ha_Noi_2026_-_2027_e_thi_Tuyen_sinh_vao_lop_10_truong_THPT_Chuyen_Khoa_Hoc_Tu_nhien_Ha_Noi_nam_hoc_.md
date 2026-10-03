# Đề thi Tuyển sinh vào lớp 10 trường THPT Chuyên Khoa Học Tự nhiên Hà Nội năm học 2026-2027

- **Tỉnh/Thành phố:** Hà Nội
- **Trường:** THPT Chuyên Khoa học Tự nhiên (ĐHKHTN - ĐHQGHN)
- **Năm học:** 2026 - 2027
- **Môn thi:** Tin học (Chuyên)

---

## NỘI DUNG ĐỀ THI

%

ĐẠI HỌC QUỐC GIA HÀ NỘI ĐỀ THỊ TUYỂN SINH vhoté
TRƯỜNG ĐẠI HOC KHOA HỌC TỰ NHIÊN TRƯỜNG THPT CHUYÊN KH 026
1G ĐẠI HỌC KHOA HỌC TỰ
Đề chính thức ⁄2
MÔN THI: TIN HỌC “Wy
Thời gian làm bai: 150 phút (không kể thời gian phát đề) 4)

Đề thi gồm: 04 trang Vê)

TỔNG QUAN ĐỀ THỊ

| Bài | Tên tập chươngtrình | Dữ hiệu vào (input) | pự liệu ra (Output) _ j Giới han thời gian/ bộ nhớ | Điểm |
L SQRT.* stdin stdout | 1s/1GB_ |
2 CARD.* stdin stdout 1s/ 1GB
3 TILE.* ‘stdin stdout 18/1GB —_
4 LOTO.* stdin stdout 1s/ 16B
5 NGHT.* stdin stdout 1s/ 16B

Dấu * được thay thế bởi CPP hoặc PY tương ứng với ngôn ngữ lập trình C++ hoặc Python. Thí sinh hãy
lập trình giải các bài toán sau:

### Bài 1. SQRT

Cho một dãy gồm N số nguyên dương ay, dp, ..., đụ.
Hãy in ra số lượng phần tử trong day là số chính phương. Một số nguyên dương x được gọi là số
chính phương nếu tồn tại một số agtÿến đ#øng k sao cho k? = x.

#### Input:

Dòng đầu tiên chứa một số nguyên dương N (1 < N< 105).
Dòng thứ hai chứa N số nguyên dương az, az, ..., an ELS a; < 109, 1 < ¡ < N).

#### Output:

In ra số lượng số chính phương trong dấy..
Subtasks:
* 40% số test có ràng buộc bổ sung: W < 100, a; < 100 (1 < ¡ < N).
* 60% số test còn lại không có ràng buộc bổ sung.


#### Ví dụ:


| Sample Input Sample Output Giải thích
5 3 Có 3 số chính phương: 1 = 12, 4 = 22, 16 = 43,
1471610


### Bài 2. CARD


Bạn có W lá bài đặt thành một hàng, lá bài thứ ¡ có giá trị a). Bạn chơi trò chơi sau:
* _ Trong mỗi lượt, lấy hai lá bài ở đầu hàng bên trái ra so sánh giá trị.
* _ Nếu một lá bài có giá trị lớn hơn, lá lớn hơn này được đặt lại vào đầu hàng, lá nhỏ hơn bị loa
bỏ.
„..*- Nếu hai lá bài có giá trị bằng nhau, cả hai đều bị loại bỏ.
“Ap lại cho đến khi còn tối đa 1 lá bài

Dòng đầu tiên chứa một số nguyên dương N (1 < N < 10).
Dòng thứ hai chứa N số nguyên dương a1, dz, ... av (1 < a) < 10°, 1 < ï < N).


#### Output: @

In ra một số nguyên duy nhất: giá trị lá bài còn lại, hoặc 0 nếu không còn lá nào. 2z “4

Subtasks: “>

* 40% số test có ràng buộc bổ sung: N < 10°. đ
* 60% số test còn lại không có ràng buộc bổ sung. VÔ)

#### Ví dụ: “O

Sample Input Sample Output Giai thich
5 ip “lượt 1: so 3 và 1 > 3 lớn hơn, hàng: [3, 4, 1, 5]
31415 Lượt 2: so 3 và 4 > 4 lớn hơn, hàng: [4, 1, 5]
Lượt 3: so 4 và 1 > 4 lớn hơn, hài , 5]
Lượt 4: so 4 và 5 > 5 lớn hơn, hàng: [5]
L Còn lại: 5,
4 0 Lượt 1: so 2 và 2 > bằng, loại cả hai, hàng: [3, 3]
2233 Lượt 2: so 3 và 3 > bằng, loại cả hai, hàng: []
Không còn lá nào > 0.

### Bài 3. TILE


Bạn cần lát đầy dải ô vuông kích thước 1xN bằng các viên gạch có độ dài 1, 2, hoặc 3.
© Gach có độ dài 1 có a màu khác nhau.
* Gach có độ dài 2 có b màu khác nhau.
© Gach có độ dài 3 có c màu khác nhau.
Hai cách lát được coi là khác nhau nếu tồn tại ít nhất một ô vuông kích thước 1x1 mà viên gạch phủ
trên đó khác nhau về độ dài hoặc màu sắc.
Hãy đếm số cách lát đầy dải 1xN, kết quả lấy dư cho 998244853.

#### Input:

Dòng duy nhất chứa bốn số nguyên dương N, a, b, c (1< N < 108, 1< g, b, c < 10°).

#### Output:

In ra một số nguyên duy nhất: số cách lát dải, lấy dư cho 998244853.

Subtasks:
© 50% số test khác có ràng buộc bổ sung: W < 103,
s 50% số test còn lại không có ràng buộc bổ sung.


#### Ví dụ:

Sample Input Sample Output Giải thích

13 Ba gạch độ dài 1: 23 = 8 cách. /
211 Gạch độ dài 1 + gạch độ dài 2: 2x1 = 2 cách.

Gạch độ dài 2 + gạch độ dài 1: 1x2 = 2 cách.
Một gạch độ dài 3: 1 cách.
Tổng=8+2+2+1= 13.

%4

;ờng H tổ chức chương trình tuyển chọn học sinh cho đội tuyển chuyên. Có 2026 ên đề kiến
;c được đánh số thứ tự từ 1 đến 2026. Hội đồng chuyên môn xác định.M chuyên đề tr trong
K chuyên đề đầu tiên được xem là các chuyên đề cốt lõi quan trọng nhất.

5¡ học sinh đăng ký đúng K chuyên đề mà mình tự tin nhất (các chuyên đề đôi một khác nữ đế

+
a mức độ phù hợp giữa lựa chọn của học sinh và danh sách chuyên đề trọng tâm, hội đồng phân 0g?
yc sinh theo các nhóm năng lực sau (ưu tiên nhóm có số thứ tự nhỏ nhất mà học sinh dat được): Vô)
s_ Nhóm năng lực 1: Toàn bộ K chuyên đề đăng ký đều nằm trong K chuyên đề cốt lỗi.
s_ Nhóm nang lực 2: Toàn bộ K chuyên đề đăng ký đều nằm trong M chuyên đề trong tâm.
© Nhóm nang lực 3: Có thể chọn ra K — 1 chuyên đề (không kể thứ tự) trong danh sách đăng ký
sao cho tất cả đều thuộc K — 1 chuyên đề cốt lõi đầu tiên.
© Nhóm nang lực 4: Có thể chon ra K — 1 chuyên đề (không kể thứ tự) trong danh sách đăng ký
sao cho tất cả đều thuộc K chuyên đề cốt lõi.
s Nhóm nang lực 5: Có thể chọn ra K — 1 chuyên đề (không kể thứ tự) trong danh sách đăng ký
_ sao cho tất cả đều thuộc M chuyên đề trọng tâm.
s Nhóm năng lực 6: Có thể chọn ra K — 2 chuyên đề (không kể thứ tự) trong danh sách đăng ký
sao cho tất cả đều thuộc M chuyên đề trọng tâm.
ó J học sinh tham gia đăng ký. Mỗi học sinh được xếp vào nhóm năng lực có số thứ tự nhỏ nhất mà
›ọc sinh đó thỏa mãn điều kiện.
viét một chương trình để xác định:
e_ Nhiệm vụ 1: Số lượng học sinh được xếp vào nhóm năng lực C cụ thể. Các nhóm năng lực được
đánh số 1, 2, ..., 6, 7. Nhóm năng lực 7 dành cho những học sinh không thuộc nhóm nào ở trên.
« Nhiệm vụ 2 : Các chuyên đề nhiều học sinh dang ký nhất, được viết theo thứ tự tăng dần nếu có
nhiều hơn 1 chuvén đề thỏa mãn.


#### Input:


Dòng đầu tiên ghi mã số nhiệm vụ (1 hoặc 2).

Dòng thứ hai ghi 3 số M, K, € (1 <M < 2026, 5 < K <M,1< € < 7).

Dòng thứ ba ghi số thứ tự M chuyên đề trọng tâm, theo thứ tự ưu tiên (cốt lõi trước, mở rộng sau).
Dòng thứ tư ghi một số tự nhiên J (1 <7 <5 x 103), biểu thị số lượng học sinh, và mỗi dòng trong
số J dòng tiếp theo ghi K số tự nhiên, biểu thị các chuyên đề mà học sinh đó đăng ký.


#### Output:


Đối với nhiệm vụ 1, in ra số lượng học sinh thuộc nhóm năng lực C.

Đối với nhiệm vụ 2, in ra số thứ tự các chuyên đề được nhiều học sinh đăng ký nhất, viết theo thứ tự
tăng dần.
Subtasks:

-

© 50% còn lại không có ràng buộc gi thêm.

Nhiệm vụ 1. Hội đồng xác định 6 chuyên đề trọng tâm theo
thứ tự là 11,12,13,14,15,16. Mỗi học sinh đăng ký 5 |
chuyên đề. Có một học sinh duy nhất. Học sinh này. aa ky
được xếp vào
các chuyên đề 15,14,13,12,11. HỌC sinh ‹
Nhóm. ia đã đăng ky đúng 5 chuyên đề cốt lối đầu tiên.

1112 13 14 15 16
1

15 14 131211

Nhiệm vụ 1 Có 2 học sinh. Một trong số ho dug
Nhôm 1 và một học sinh được xếp vào Nhóm 4.

4

5
1222374 2526 lượng học sinh thuộc Nhóm 4, kết quả là 1

921252322
321252224

we

Cø 3 học sinh. Không ai trong số he thuộc bất ky nhóm nào
từ 1 đến 6.

1
657

91 92 33 94 9S %6
3

2356814
13471829
12327493

654
71 72 73 74 75 76
2

79 71 75 7372
7371757274

Nhiệm vụ 2. Các chuyển đề 71, 72, 73, 75 đều được cả hai
học sinh đăng ky, nên chung là các chuyên đề được nhiều.
học sinh đẳng ký nhất.

11 12 73 75


### Bài 5. NGHT


on mã (6 5) tấn cỗng các 6 vuông (đấu x) trên bàn cờ như hình dưới. Có một ban cờ kích thước 4xn,
ởi 4 hang và n cột, trong đó 1 < n < 100. Gọi Z là tập các 6 trên bàn cờ. Các hàng được đánh số thứ tự
£ trên xuống đưới, từ 1 đến 4, các cột được đánh số thứ tự từ trái qua phải, từ 1 đến n. Quan mã chi
+ thế được đặt trên các 6 không thuộc Z và hai quân bat kỳ không được ăn nhau
ia định trong mỗi cột có nhiều nhất một ô thuộc Z. Vi vậy, tập Z có thé được mô tả
ang chuỗi kz, kạ,...k„ trong do k, thuộc {0,1,2,3,4}. Nếu k, = 0 thì cột Ì không có ô nào
uộc Z, ngược lại, ô ở hàng k,„ cột i thuộc Z.

ny tinh số lượng tối đa của các quan ma M, có thé đặt trên ban cơ theo quy tắc trên

va số lượng L cách sắp xếp có thế có của M quân mã trên ban cờ nay.

My Jz Js | [z Js]
Dong đầu tiên là số nguyên dương n (1 < n < 100). isis] |s[ |
Nỗi dong trong n dòng sau ghi một số 0, 1, 2, 3 hoặc 4. Hy | Is |


#### Output:


in ra hai số M và L. Z| | iz] | {zt | ge
« 50% số test có ràng buộc bố sung: n s 25. tê) S| SS a

« 50% số test còn lại không có rang buộc bố sung.

Xếp được tối đa 4 con mã và có 8 cách bố

trí hợp lẽ như hình trên.

~— HET ---

———————_
Cần bộ coi thi không giỏi thích gì thêm.