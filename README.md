# Hệ Thống Quản Lý Bán Sách Theo Kiến Trúc Microservices

## 1. Giới thiệu

Dự án này xây dựng một **hệ thống quản lý bán sách** dựa trên **kiến trúc Microservices**.  
Hệ thống được chia thành nhiều dịch vụ độc lập, mỗi dịch vụ đảm nhiệm một chức năng riêng trong hệ thống.

Mỗi service:

- Chạy trong một container Docker riêng
- Cung cấp RESTful API
- Giao tiếp với các service khác thông qua HTTP

Hệ thống hỗ trợ các chức năng chính:

- Quản lý khách hàng
- Quản lý sách
- Quản lý giỏ hàng
- Quản lý đơn hàng
- Thanh toán
- Vận chuyển
- Đánh giá và nhận xét sách
- Gợi ý sách bằng AI

---

# 2. Kiến trúc hệ thống

Hệ thống được xây dựng theo mô hình **Microservices Architecture**.

Đặc điểm:

- Mỗi service chạy độc lập
- Giao tiếp qua REST API
- Mỗi service có port riêng
- Tất cả được quản lý bằng **Docker Compose**

Ưu điểm:

- Dễ mở rộng
- Dễ bảo trì
- Có thể phát triển độc lập từng service

---

# 3. Danh sách Service

| Service | Port | Mô tả |
|------|------|------|
| API Gateway | 8000 | Điểm truy cập chính của hệ thống |
| Customer Service | 8001 | Quản lý khách hàng |
| Book Service | 8002 | Quản lý thông tin sách |
| Cart Service | 8003 | Quản lý giỏ hàng |
| Order Service | 8004 | Quản lý đơn hàng |
| Catalog Service | 8005 | Quản lý danh mục sách |
| Staff Service | 8006 | Quản lý nhân viên |
| Manager Service | 8007 | Quản lý hệ thống |
| Comment & Rating Service | 8008 | Quản lý đánh giá sách |
| Payment Service | 8009 | Xử lý thanh toán |
| Shipping Service | 8010 | Quản lý vận chuyển |
| Recommender AI Service | 8011 | Gợi ý sách |

---

# 4. Danh sách API

## 4.1 Customer Service

Base URL

```
http://localhost:8001
```

| Method | Endpoint | Chức năng |
|------|------|------|
| GET | /customers/ | Lấy danh sách khách hàng |
| POST | /customers/ | Tạo khách hàng |
| GET | /customers/{id}/ | Lấy thông tin khách hàng |
| PUT | /customers/{id}/ | Cập nhật khách hàng |
| DELETE | /customers/{id}/ | Xóa khách hàng |

---

## 4.2 Book Service

Base URL

```
http://localhost:8002
```

| Method | Endpoint | Chức năng |
|------|------|------|
| GET | /books/ | Lấy danh sách sách |
| POST | /books/ | Thêm sách |
| GET | /books/{id}/ | Lấy thông tin sách |
| PUT | /books/{id}/ | Cập nhật sách |
| DELETE | /books/{id}/ | Xóa sách |

---

## 4.3 Cart Service

Base URL

```
http://localhost:8003
```

| Method | Endpoint | Chức năng |
|------|------|------|
| GET | /carts/ | Lấy danh sách giỏ hàng |
| POST | /carts/ | Tạo giỏ hàng |
| GET | /cart-items/ | Lấy sản phẩm trong giỏ |
| POST | /cart-items/ | Thêm sản phẩm vào giỏ |
| DELETE | /cart-items/{id}/ | Xóa sản phẩm khỏi giỏ |

---

## 4.4 Order Service

Base URL

```
http://localhost:8004
```

| Method | Endpoint | Chức năng |
|------|------|------|
| GET | /orders/ | Lấy danh sách đơn hàng |
| POST | /orders/ | Tạo đơn hàng |
| GET | /orders/{id}/ | Lấy thông tin đơn hàng |
| PUT | /orders/{id}/ | Cập nhật đơn hàng |
| DELETE | /orders/{id}/ | Hủy đơn hàng |

---

## 4.5 Catalog Service

Base URL

```
http://localhost:8005
```

| Method | Endpoint | Chức năng |
|------|------|------|
| GET | /categories/ | Lấy danh sách danh mục |
| POST | /categories/ | Tạo danh mục |
| GET | /categories/{id}/ | Lấy thông tin danh mục |
| PUT | /categories/{id}/ | Cập nhật danh mục |
| DELETE | /categories/{id}/ | Xóa danh mục |

---

## 4.6 Staff Service

Base URL

```
http://localhost:8006
```

| Method | Endpoint | Chức năng |
|------|------|------|
| GET | /staff/ | Lấy danh sách nhân viên |
| POST | /staff/ | Thêm nhân viên |
| GET | /staff/{id}/ | Lấy thông tin nhân viên |
| PUT | /staff/{id}/ | Cập nhật nhân viên |
| DELETE | /staff/{id}/ | Xóa nhân viên |

---

## 4.7 Manager Service

Base URL

```
http://localhost:8007
```

| Method | Endpoint | Chức năng |
|------|------|------|
| GET | /managers/ | Lấy danh sách quản lý |
| POST | /managers/ | Tạo quản lý |
| GET | /managers/{id}/ | Lấy thông tin quản lý |
| PUT | /managers/{id}/ | Cập nhật quản lý |
| DELETE | /managers/{id}/ | Xóa quản lý |

---

## 4.8 Comment & Rating Service

Base URL

```
http://localhost:8008
```

| Method | Endpoint | Chức năng |
|------|------|------|
| GET | /ratings/ | Lấy danh sách đánh giá |
| POST | /ratings/ | Tạo đánh giá |
| GET | /ratings/{id}/ | Lấy thông tin đánh giá |
| PUT | /ratings/{id}/ | Cập nhật đánh giá |
| DELETE | /ratings/{id}/ | Xóa đánh giá |

---

## 4.9 Payment Service

Base URL

```
http://localhost:8009
```

| Method | Endpoint | Chức năng |
|------|------|------|
| GET | /payments/ | Lấy danh sách thanh toán |
| POST | /payments/ | Tạo thanh toán |
| GET | /payments/{id}/ | Lấy thông tin thanh toán |

---

## 4.10 Shipping Service

Base URL

```
http://localhost:8010
```

| Method | Endpoint | Chức năng |
|------|------|------|
| GET | /shipments/ | Lấy danh sách vận chuyển |
| POST | /shipments/ | Tạo thông tin vận chuyển |
| GET | /shipments/{id}/ | Lấy thông tin vận chuyển |
| PUT | /shipments/{id}/ | Cập nhật vận chuyển |

---

## 4.11 Recommender AI Service

Base URL

```
http://localhost:8011
```

| Method | Endpoint | Chức năng |
|------|------|------|
| GET | /recommendations/ | Lấy danh sách sách gợi ý |

---

# 5. Công nghệ sử dụng

| Thành phần | Công nghệ |
|------|------|
| Backend Framework | Django REST Framework |
| Ngôn ngữ | Python |
| Container | Docker |
| Container Orchestration | Docker Compose |
| API Communication | RESTful API |
| Database | SQLite |

---

# 6. Chạy hệ thống

Chạy toàn bộ hệ thống

```
docker-compose up --build
```

Dừng hệ thống

```
docker-compose down
```

---

# 7. Migration cơ sở dữ liệu

Chạy migration cho một service

```
docker compose exec <service_name> python manage.py migrate
```

Ví dụ

```
docker compose exec customer-service python manage.py migrate
```

---
