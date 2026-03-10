Hệ Thống Quản Lý Bán Sách Theo Kiến Trúc Microservices
1. Giới thiệu

Dự án này xây dựng một hệ thống quản lý bán sách dựa trên kiến trúc Microservices.
Hệ thống được chia thành nhiều dịch vụ độc lập, mỗi dịch vụ đảm nhiệm một chức năng cụ thể trong hệ thống.

Mỗi service:

Chạy trong một container Docker riêng

Cung cấp các RESTful API

Giao tiếp với các service khác thông qua HTTP

Hệ thống hỗ trợ các chức năng chính:

Quản lý khách hàng

Quản lý sách

Quản lý giỏ hàng

Quản lý đơn hàng

Thanh toán

Vận chuyển

Đánh giá và nhận xét sách

Gợi ý sách bằng AI

2. Kiến trúc hệ thống

Hệ thống được xây dựng theo kiến trúc Microservices, trong đó mỗi service chịu trách nhiệm cho một phần chức năng của hệ thống.

Đặc điểm của kiến trúc:

Mỗi service được triển khai độc lập

Các service giao tiếp thông qua REST API

Mỗi service có port riêng

Tất cả các service được quản lý bằng Docker Compose

Kiến trúc này giúp hệ thống:

Dễ mở rộng

Dễ bảo trì

Cho phép phát triển độc lập từng service

3. Danh sách các Service
Service	Port	Mô tả
API Gateway	8000	Điểm truy cập trung tâm của hệ thống, nhận request từ client và chuyển tiếp đến các service
Customer Service	8001	Quản lý thông tin khách hàng
Book Service	8002	Quản lý thông tin sách
Cart Service	8003	Quản lý giỏ hàng của khách hàng
Order Service	8004	Xử lý và quản lý đơn hàng
Catalog Service	8005	Quản lý danh mục sách
Staff Service	8006	Quản lý thông tin nhân viên
Manager Service	8007	Quản lý hệ thống ở cấp quản trị
Comment and Rating Service	8008	Quản lý đánh giá và nhận xét của khách hàng
Payment Service	8009	Xử lý thanh toán
Shipping Service	8010	Quản lý vận chuyển đơn hàng
Recommender AI Service	8011	Cung cấp gợi ý sách cho khách hàng
4. Danh sách API
4.1 Customer Service

Base URL

http://localhost:8001
Method	API	Chức năng
GET	/customers/	Lấy danh sách khách hàng
POST	/customers/	Tạo khách hàng mới
GET	/customers/{id}/	Lấy thông tin khách hàng
PUT	/customers/{id}/	Cập nhật thông tin khách hàng
DELETE	/customers/{id}/	Xóa khách hàng
4.2 Book Service

Base URL

http://localhost:8002
Method	API	Chức năng
GET	/books/	Lấy danh sách sách
POST	/books/	Thêm sách mới
GET	/books/{id}/	Lấy thông tin sách
PUT	/books/{id}/	Cập nhật sách
DELETE	/books/{id}/	Xóa sách
4.3 Cart Service

Base URL

http://localhost:8003
Method	API	Chức năng
GET	/carts/	Lấy danh sách giỏ hàng
POST	/carts/	Tạo giỏ hàng
GET	/cart-items/	Lấy danh sách sản phẩm trong giỏ
POST	/cart-items/	Thêm sản phẩm vào giỏ
DELETE	/cart-items/{id}/	Xóa sản phẩm khỏi giỏ
4.4 Order Service

Base URL

http://localhost:8004
Method	API	Chức năng
GET	/orders/	Lấy danh sách đơn hàng
POST	/orders/	Tạo đơn hàng
GET	/orders/{id}/	Lấy thông tin đơn hàng
PUT	/orders/{id}/	Cập nhật đơn hàng
DELETE	/orders/{id}/	Hủy đơn hàng
4.5 Catalog Service

Base URL

http://localhost:8005
Method	API	Chức năng
GET	/categories/	Lấy danh sách danh mục
POST	/categories/	Tạo danh mục
GET	/categories/{id}/	Lấy thông tin danh mục
PUT	/categories/{id}/	Cập nhật danh mục
DELETE	/categories/{id}/	Xóa danh mục
4.6 Staff Service

Base URL

http://localhost:8006
Method	API	Chức năng
GET	/staff/	Lấy danh sách nhân viên
POST	/staff/	Thêm nhân viên
GET	/staff/{id}/	Lấy thông tin nhân viên
PUT	/staff/{id}/	Cập nhật nhân viên
DELETE	/staff/{id}/	Xóa nhân viên
4.7 Manager Service

Base URL

http://localhost:8007
Method	API	Chức năng
GET	/managers/	Lấy danh sách quản lý
POST	/managers/	Tạo quản lý
GET	/managers/{id}/	Lấy thông tin quản lý
PUT	/managers/{id}/	Cập nhật quản lý
DELETE	/managers/{id}/	Xóa quản lý
4.8 Comment and Rating Service

Base URL

http://localhost:8008
Method	API	Chức năng
GET	/ratings/	Lấy danh sách đánh giá
POST	/ratings/	Tạo đánh giá
GET	/ratings/{id}/	Lấy thông tin đánh giá
PUT	/ratings/{id}/	Cập nhật đánh giá
DELETE	/ratings/{id}/	Xóa đánh giá
4.9 Payment Service

Base URL

http://localhost:8009
Method	API	Chức năng
GET	/payments/	Lấy danh sách thanh toán
POST	/payments/	Tạo thanh toán
GET	/payments/{id}/	Lấy thông tin thanh toán
4.10 Shipping Service

Base URL

http://localhost:8010
Method	API	Chức năng
GET	/shipments/	Lấy danh sách vận chuyển
POST	/shipments/	Tạo thông tin vận chuyển
GET	/shipments/{id}/	Lấy thông tin vận chuyển
PUT	/shipments/{id}/	Cập nhật vận chuyển
4.11 Recommender AI Service

Base URL

http://localhost:8011
Method	API	Chức năng
GET	/recommendations/	Lấy danh sách sách gợi ý
5. Công nghệ sử dụng
Thành phần	Công nghệ
Backend Framework	Django REST Framework
Ngôn ngữ lập trình	Python
Container	Docker
Quản lý container	Docker Compose
Giao tiếp API	RESTful API
Cơ sở dữ liệu	SQLite
6. Chạy hệ thống

Để chạy toàn bộ hệ thống bằng Docker Compose:

docker-compose up --build

Dừng hệ thống:

docker-compose down
7. Migration cơ sở dữ liệu

Để chạy migration cho một service:

docker compose exec <service_name> python manage.py migrate

Ví dụ:

docker compose exec customer-service python manage.py migrate
