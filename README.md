## Omnichannel

Omnichannel là chiến lược hợp nhất dữ liệu và trải nghiệm khách hàng trên mọi điểm chạm - online và offline - để doanh nghiệp hiểu khách hàng hơn và phản ứng đúng thời điểm.


## Mô tả
### Giai đoạn 1: Thu thập hành vi Online (Website, FB, Messenger)
**Bối cảnh**:
Khách thấy quảng cáo click vào website hoặc tương tác post FB, nhắn Mess

**Flow dữ liệu**:
1. Website/FB thu thập dữ liệu dưới dạng ẩn danh
2. Hành vi phát sinh event:
- view_menu
- search menu
- like/comment post
3. Event gửi vào hệ thống

**Mục đích**:
- Chưa cần tối ưu hóa hành vi theo từng khách hàng
- Thu thập dữ liệu phục vụ đánh giá xu hướng chung

----
### Giai đoạn 2: Gắn định danh khách hàng
**Bối cảnh**:
Website pop-up/ Mess chủ động xin số điện thoại(optional)

**Flow dữ liệu**:
1. Khách nhập số điện thoại
2. Map hành vi gđ1

**Mục đích**:
- Toàn bộ hành vi trước đó được gắn vào khách hàng cụ thể
- Cá nhân hóa dữ liệu

----
### Giai đoạn 3: Instore: Hợp nhất online & offline
**Bối cảnh**:
Khách đến quán, quét QR mở menu app.

**Flow dữ liệu**:
1. Ở đây pop-up đky tkhoan nếu trùng thông tin online -> lấy dữ liệu lịch sử match

**Mục đích**:
- Hành vi online & tại quán được hợp nhất
- Cá nhân hóa realtime gợi ý món ăn, combo họ tương tác khi chưa tới quán
- Upsell sau khi khách dùng bữa xong = cho voucher khi khách thỏa mãn điều kiện ()

**Chú ý**:
- Có thể dùng redis ở, Redis lưu trữ các trạng thái ngắn hạn đã được xử lý (như hành vi gần nhất, điều kiện nhận ưu đãi, thời điểm tương tác) nhằm hỗ trợ cá nhân hóa và cấp voucher theo ngữ cảnh tức thời với độ trễ thấp

----
### Giai đoạn 4: Batch processing làm giàu dữ liệu
**Bối cảnh**:
Cuối ngày

**Flow dữ liệu**:
1. Tổng hợp:
- View → Order
- Món ưa thích
- Tần suất ghé

2. Cập nhật
- Customer profile
- Feature table

**Mục đích**:
- Tăng trải nghiệm khách hàng
- Giảm phụ thuộc rule -> sẵn sàng cho ML

----
### Giai đoạn 5 – Comeback: Vòng lặp dữ liệu
**Bối cảnh**:
Khách quay lại quán.

**Flow dữ liệu**:
- Dữ liệu mới → streaming + batch

**Mục đích**:
- Hồ sơ khách ngày càng chính xác
- Cá nhân hóa tốt hơn mỗi lần
