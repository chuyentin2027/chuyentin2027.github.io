# Đề thi thử Tuyển sinh lớp 10 trường THPT chuyên Đại học Sư Phạm năm học 2025

- **Tỉnh/Thành phố:** Hà Nội
- **Trường:** THPT Chuyên Đại học Sư phạm Hà Nội
- **Năm học:** 2025 - 2026
- **Môn thi:** Tin học (Chuyên)

---

## NỘI DUNG ĐỀ THI

BỘ GIÁO DỤC VÀ ĐÀO TẠO
TRƯỜNG ĐẠI HỌC SU PHẠM HÀ NỘI
TRƯỞNG
ĐỂ THỊ THAM KAHỌC
(Để thi gồm co 3 Hrang
SỰ PHAM
HA NỘI
DAO
KỲ THI TUYẺN SINH LỚP 10
TRƯỜNG THPT CHUYỀN ĐẠI HỌC SƯ PHẠM NĂM 2025
MÔN: TIN HỌC
Dùng riêng cho thí sinh thi vào lớp chuyên Tin học
Thời gian làm bài: 150 phút (không kể thời gian phát để)
Chú ý
STT
Tên bài
Tên file bài làm

#### Giới hạn mỗi test

Điểm
1
Số chính phương
BAI1.
1 giäy/1 GB
3.0
2
Hội thao
BAI2.
1 giäy/1 GB
2.5
3
Robot
BAI3.
1 giäy/1 GB
2.5
4
Tinh thể
BAI4.
1 giây/1 GB
2.0

#### Dữ liệu vào đúng đắn khôngcần kiểm tra;

GIAO
Dẩu * được thay bằng cpp, c, pas, py tùy theo ngôn ngữlập trình được sử dụng (C++, C, Pascal hay Python
Chương trình sử dụng cơ chế nhập/xuất dữ liệu từ thiết bị nhập chuẩn (standard input) và thiết bị xuất chuan
(standard output), không được phép đọc/ghi bất kỳ tệp (file) nào trên máy tính.
Cấu hình dịch để chấm bài.
C++ (GNU G++ 9.2): -std=c++14 -02 -s -static-lm -x c++
C (GNU GCC 9.2): -std=c11-02-s -static -lm -х с
Pascal (Free Pascal 3.0.4): -02 -XS-Sg
Python (Python 3): Chạy trực tiếp mã nguồn qua thông dịch
Hãy lập chương trình giải quyết các bài toán sau đây:

### Bài 1 (3.0 điểm). SỐ CHÍNH PHƯƠNG (BAII.*)

Số chính phương là số tự nhiên có căn bậc hai là một số tự nhiên. Ví du 1, 4, 9, ... là các số chính
phương.

#### Yêu cầu: Đếm các cặp nguyện dương (i,j) thỏa mãn điều kiện:

1si<j≤n
li x j là số chính phương
Dữ liệu: Vào từ thiết bị nhập chuẩn ghi duy nhất số nguyên dương n (n≤ 105).
Kết quả: Ghỉ ra thiết bị xuất chuẩn một số nguyên duy nhất là số cặp (i,j) tìm được.

#### Ví dụ

Sample Input
Sample Output
Giải thích
4
6
Có 6 cặp thỏa mãn là:
(1,1); (1,4); (2,2); (3,3); (4,1); (4,4).
60% số điểm ứng với các test có 1≤ n ≤ 5000
40% số điểm còn lại không có ràng buộc bố sung

### Bài 2 (2.5 điểm). HỘI THAO (BAI2.*)

Đoàn trường X tổ chức hội thao với nhiều nội dung thi đấu sôi động. Một trong những nội dung đặc
biệt là đua xe đạp đôi, trong đó hai vận động viên cùng ngồi trên một chiếc xe đạp và phối hợp di chuyển
theo lộ trình đã định. Ban tổ chức có danh sách n vận động viên, được đánh số từ 1 đến n, với trọng
Trang 1/3
DUC
TRƯỜ
ĐẠI HO
SƯ PH
HÀ NC
chuyentin.pro

lượng lần lượt là a1,a2,..., an kg. Mỗi chiếc xe đạp có trọng tải tối đa là p kg, nên cần chọn ra hai vận
động viên có tổng trọng lượng không vượt quá p để tham gia.

#### Yêu cầu: Bạn hãy giúp Ban tổ chức đếm số cách chọn hai vận động viên để làm mẫu.

Dữ liệu: Vào từ thiết bị nhập chuẩn
Dòng đầu tiên chứa 2 số nguyên n và p (2 ≤n ≤ 2*105,1 ≤p ≤ 109) - số lượng vận động viên
và trọng tải của xe đạp.
Dòng thứ hai chứa n số nguyên a1,a2,..., an (1 ≤ a ≤ 10) - tương ứng là trọng lượng của n vận
động viên.
Kết quả: Ghi ra thiết bị xuất chuẩn một số nguyên là số cách chọn một cặp vận động viên để làm mẫu.

#### Ví dụ

Sample Input
59
4841 10
Sample Output
4
* 60% số điểm ứng với các test có n ≤ 1000.
40% số điểm còn lại không có ràng buộc bổ sung.

### Bài 3 (2.5 điểm). ROBOT (BAI3.*)

Trong một thành phố tương lai, các robot có khả năng tự học hỏi và phát triển kỹ năng ngôn ngữ để
giao tiếp với con người. Một trong số đó là Robot Alpha, một robot tiên tiến nhưng gặp vấn đề trong
việc nhận diện và sắp xếp thông tin văn bản. Để giúp Alpha cải thiện khả năng này, một bài kiểm tra
đặc biệt đã được thiết kế. Robot Alpha sẽ được cụng cấp một chuỗi dữ liệu hỗn loạn và cần phải tái tạo
lại một chuỗi mục tiêu đã được mã hóa. Tuy nhiên, Alpha không thể tự do nhập ký tự mà phải tuân theo
quy tắc di chuyển đặc biệt.
Cách Robot Alpha hoạt động:
Di chuyển liền kề:
10
Alpha có thể di chuyển đến ký tự kề bên trái hoặc kề bên phải trong chuỗi hiện tại và sao chép ký
tự đó vào kết quả.
Di chuyển bằng kết nối dữ liệu:
Alpha có thể dịch chuyển đến bất kỳ vị trí nào trong chuỗi có cùng ký tự với vị trí hiện tại mà
không cần sao chép ký tự vào kết quả.
* Điều này giúp Alpha di chuyển nhanh hơn mà không thay đổi nội dung của kết quả.
Việc di chuyển tốn |x - y| giây, trong đó x và y là vị trí của ký tự ban đầu và ký tự mới.

#### Yêu cầu: Alpha phải tạo ra chuỗi mã hóa mục tiêu trong thời gian ngắn nhất.

Dữ liệu: Vào từ thiết bị nhập chuẩn
發Dòng đầu tiên chứa một số nguyên n, m (1 ≤ n, m ≤ 3000).
Dòng thứ hai chứa n kí tự in thường, là chuỗi dữ liệu hỗn loạn ban đầu.
Dòng thứ ba chứa chuỗi mục tiêu được mã hóa.
Kết quá: Ghi ra thiết bị xuất chuẩn in ra thời gian ngắn nhất. Nếu không tạo được chuỗi mục tiêuy
thì in ra -1.
Trang 2/3
chuyentin.pro


#### Ví dụ

Sample Input
Sample Output
Giải thích test 2
22
-1
Wa
ac
7
10 5
Doofenferb
feren
Alpha xuất phát từ vị trí thứ 7 và sao chép kí tự 'f'.
Sau đó Alpha di chuyển sang phải hai lần, sao chép
Lần lượt kí tự 'e', 'r'. Tiếp theo, Alpha di chuyễn sang
trái một lần, sao chép kí tự 'e'. Sau đó bằng cách hai,
Alpha di chuyển đến vị trí thứ 5. Cuối cùng di chuyển
sang phải một lần, sao chép kí tự 'n'. Tổng cộng mất
thời gian là 7 giây.
50% số điểm ứng với các test có 1 ≤n, m ≤ 300.
50% số điểm còn lại không có ràng buộc bổ sung.

### Bài 4 (2 điểm). TINH THE (BAI4.*)

Bạn là một phi hành gia đang thực hiện nhiệm vụ khám phá một hành tinh xa xôi. Con tàu của bạn đã
hạ cánh xuống bề mặt hành tỉnh, và bạn cần thu thập các tinh thể năng lượng để duy trì hệ thống sự sống
của mình.
Trên hành tinh này có n điểm thu thập tinh thể được đánh số từ 1 đến n. Mỗi điểm thu thập chứa một
tinh thể có giá trị năng lượng a. Nếu a là số dương, bạn nhận thêm năng lượng. Nếu a là số âm, bạn
sẽ bị tiêu hao năng lượng nếu thu thập tinh thể này. Bạn có thể chọn thu thập hoặc bỏ qua từng tinh thể,
nhưng tổng năng lượng của bạn không bao giờ được phép âm. Mục tiêu của bạn là thu thập nhiều tỉnh
thể nhất có thể khi di chuyển từ điểm đầu tiên đến điểm cuối cùng.
Dữ liệu: Vào từ thiết bị nhập chuẩn
Dòng đầu tiên chứa một số nguyên n (1 ≤n ≤2x 105) - số điểm thu thập tinh thể.
Dòng thứ hai chứa n số nguyên a (-109 ≤ a ≤ 109) - giá trị năng lượng của từng tinh thể.
Kết quả: Ghi ra thiết bị xuất chuẩn một số nguyên duy nhất - số lượng tinh thể tối đa.

#### Ví dụ

Sample Input
Sample Output
6
5
|Giải thích
Bạn có thể thu thập 5 tinh thể
1, 3, 4, 5, 6
4-4 1-3 1-3
50% số điểm ứng với các test có 1 ≤n ≤ 2000.
50% số điểm còn lại không có ràng buộc bổ sung.
HÉT
Ghi chú: Thí sinh không được sử dụng tài liệu. Cán bộ coi thi không giải thích gì thêm.
Họ tên thí sinh:.
.Số báo danh:
Trang 3/3
chuyentin.pro