# Math Game - Game đố toán đơn giản bằng Python

Một trò chơi đố toán chạy trên terminal, viết bằng Python. Chương trình đưa ra các phép tính ngẫu nhiên (cộng, trừ, nhân, chia), người chơi nhập kết quả. Trả lời đúng thì được cộng điểm và tiếp tục, trả lời sai thì game kết thúc.

## Tính năng

- Tạo câu hỏi ngẫu nhiên với 4 phép tính: `+`, `-`, `*`, `/`
- Hai số trong mỗi câu hỏi được chọn ngẫu nhiên từ 1 đến 10
- Tính điểm: mỗi câu đúng được 1 điểm
- Chơi liên tục cho đến khi trả lời sai, sau đó hiển thị tổng điểm

## Yêu cầu

- Python 3.6 trở lên (code dùng f-string)
- Không cần cài thêm thư viện nào, chỉ dùng thư viện chuẩn `random` và `operator`

## Cách chạy

1. Tải hoặc clone project về máy.
2. Mở thư mục project bằng VS Code (hoặc terminal).
3. Chạy lệnh:

```bash
python math_game.py
```

> Nếu file của bạn có tên khác, thay `math_game.py` bằng tên file thực tế.

## Cách chơi

Chương trình hiện câu hỏi, bạn nhập đáp án rồi nhấn Enter:

```text
ket qua cua 7 + 3
nhap ket qua: 10
chinh xac !
ket qua cua 6 * 4
nhap ket qua: 20
sai
======== Game Over ========
diem cua ban la 1
co gang hon nhe!
```

## Cấu trúc code

| Hàm | Chức năng |
|---|---|
| `cauhoi_ngaunhien()` | Chọn ngẫu nhiên 2 số và 1 phép tính, in câu hỏi ra màn hình và trả về đáp án đúng |
| `hoicauhoi()` | Gọi `cauhoi_ngaunhien()`, nhận đáp án từ người chơi và trả về `True` nếu đúng, `False` nếu sai |
| `game()` | Vòng lặp chính: hỏi liên tục, cộng điểm khi đúng, kết thúc khi sai và in điểm cuối |

Các phép tính được lưu trong một dictionary ánh xạ ký hiệu sang hàm của module `operator`:

```python
operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}
```

## Hạn chế hiện tại

- **Phép chia** dùng `truediv` nên kết quả là số thực. Ví dụ `7 / 3 = 2.3333333333333335`, người chơi gần như không thể nhập đúng chính xác. Chỉ các phép chia hết (như `8 / 4`) mới trả lời đúng được.
- Nếu người chơi nhập chữ thay vì số, chương trình sẽ báo lỗi `ValueError` và dừng.
- Chưa lưu điểm cao nhất giữa các lần chơi.

## Hướng phát triển

- Chỉ tạo phép chia chia hết, hoặc làm tròn kết quả đến 2 chữ số thập phân
- Bắt lỗi khi người dùng nhập không phải số (`try/except`)
- Thêm mức độ khó (khoảng số lớn hơn, thêm phép tính)
- Lưu bảng điểm cao vào file
- Giới hạn thời gian trả lời cho mỗi câu

## Tác giả

Quý
