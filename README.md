# Website Quản Lý Bán Đồ Lưu Niệm  
**Đồ án môn Phân tích và Thiết kế Hệ thống Thông tin**  
**Sinh viên thực hiện:** Trịnh Quang Hưng – 22D190070  
**Giảng viên hướng dẫn:** ThS. Nguyễn Thị Hội  
**Năm học:** 2024-2025  

![Banner dự án](https://i.imgur.com/0kDqJ9P.png)  
*Giao diện trang chủ website bán đồ lưu niệm (mockup)*

## Giới thiệu dự án
Dự án xây dựng một **website thương mại điện tử chuyên bán đồ lưu niệm** với đầy đủ các chức năng quản trị và bán hàng trực tuyến, phù hợp với xu hướng cá nhân hóa quà tặng và lưu giữ kỷ niệm tại Việt Nam hiện nay.

Website hỗ trợ 3 nhóm người dùng chính:
- **Khách hàng**: Đăng ký, tìm kiếm, mua sắm, theo dõi đơn hàng, xác nhận nhận hàng/hoàn trả.
- **Nhân viên**: Quản lý sản phẩm, đơn hàng, khách hàng.
- **Quản trị viên**: Quản lý nhân viên, tài khoản, phân quyền, lập báo cáo doanh thu & tồn kho.

## Các tính năng chính
- Đăng nhập / Đăng ký tài khoản
- Tìm kiếm & xem chi tiết sản phẩm
- Giỏ hàng & thanh toán (COD + chuyển khoản)
- Quản lý đơn hàng (xác nhận, theo dõi, hủy, hoàn tiền)
- Quản lý sản phẩm, khách hàng, nhân viên
- Phân quyền tài khoản (Admin / Nhân viên / Khách hàng)
- Báo cáo doanh thu, tồn kho, nhập/xuất hàng

## Công nghệ sử dụng
| Layer         | Công nghệ đề xuất                                  |
|---------------|-----------------------------------------------------|
| Frontend      | HTML, CSS, JavaScript, React (hoặc Vue)            |
| Backend       | PHP hoặc Node.js                                   |
| Database      | Microsoft SQL Server 2019                          |
| Bảo mật       | SSL/TLS, Firewall, mã hóa mật khẩu                 |

## Các mô hình UML đã sử dụng trong báo cáo

| STT | Tên mô hình                        | Số lượng | Mục đích sử dụng                                   |
|-----|------------------------------------|----------|----------------------------------------------------|
| 1   | Use Case Diagram (tổng + chi tiết) | 9 biểu đồ| Mô tả các chức năng hệ thống và tương tác người dùng |
| 2   | Class Diagram                      | 1        | Mô tả cấu trúc lớp và mối quan hệ dữ liệu          |
| 3   | Sequence Diagram                   | 11       | Mô tả luồng xử lý của từng Use Case                |
| 4   | Statechart Diagram                 | 17       | Mô tả trạng thái của các đối tượng chính          |
| 5   | Communication Diagram              | 8        | Mô tả tương tác giữa các đối tượng                 |
| 6   | Activity Diagram                   | 11       | Mô tả quy trình nghiệp vụ chi tiết                 |
| 7   | Package Diagram                    | 1        | Phân chia module hệ thống                          |
| 8   | Component Diagram                  | 1        | Mô tả các thành phần phần mềm                      |
| 9   | Deployment Diagram                 | 1        | Mô tả kiến trúc triển khai                         |
| 10  | ER Diagram (chuẩn hóa 3NF)         | 1        | Thiết kế cơ sở dữ liệu                             |
| 11  | Navigation Map (Sitemap)           | 4        | Thiết kế luồng điều hướng cho từng vai trò         |

## Một số hình ảnh giao diện (mockup)

<div align="center">
  <img src="https://i.imgur.com/XuZ5vP8.png" width="48%" alt="Trang chủ" />
  <img src="https://raw.githubusercontent.com/hugqag/Analyzing-the-system-selling-souvenirs/refs/heads/main/IMG_20251125_104935.jpg" width="48%" alt="Quản lý sản phẩm" />
  <br><br>
  <img src="https://i.imgur.com/fG7hJ2d.png" width="48%" alt="Giỏ hàng & thanh toán" />
  <img src="https://i.imgur.com/RtY8pQw.png" width="48%" alt="Quản lý đơn hàng" />
</div>

## Cấu trúc thư mục báo cáo

25_TRỊNH QUANG HƯNG_22D190070_PTTK web lưu niệm.docx
├── Lời mở đầu & Mục lục
├── Đặc tả bài toán (yêu cầu chức năng & phi chức năng)
├── Phân tích hệ thống (Use Case, Class, Sequence, Activity…)
├── Thiết kế hệ thống (giao diện, CSDL, sơ đồ khối, mã giả)
├── Kết luận & hướng phát triển
└── Tài liệu tham khảo
  
## Tài liệu đính kèm
- [Báo cáo đầy đủ (file Word)](https://github.com/hugqag/Analyzing-the-system-selling-souvenirs/raw/refs/heads/main/25_TR%E1%BB%8ANH%20QUANG%20H%C6%AFNG_22D190070_PTTK%20web%20l%C6%B0u%20ni%E1%BB%87m.docx)

  
**Cảm ơn cô Nguyễn Thị Hội đã hướng dẫn tận tình!**  
**Liên hệ:** hungtrinhquang2004@gmail.com
