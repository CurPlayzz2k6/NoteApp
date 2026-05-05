# 📝 PERSONAL NOTE APPLICATION - ỨNG DỤNG FIREBASE

## 1. Thông Tin Sinh Viên
* **Họ và tên:** Nguyễn Hữu Nhẩn
* **MSSV:** 24120206
* **Lớp:** 24CTT3
* **Môn học:** Tư duy tính toán
* **Giảng viên:** Lê Đức Khoan
* **Bài tập:** Lab số 2 - Xây dựng ứng dụng với API và Firebase

## 2. Giới Thiệu Ứng Dụng
Đây là ứng dụng ghi chú cá nhân (Personal Note App) được thiết kế theo mô hình tách biệt rõ ràng giữa **Frontend** và **Backend**. Ứng dụng tập trung vào tính bảo mật và trải nghiệm lưu trữ dữ liệu trực tuyến.

**Các tính năng chính:**
* **Xác thực người dùng:** Đăng ký và đăng nhập bảo mật bằng Email/Mật khẩu thông qua Firebase Authentication.
* **Quản lý ghi chú:** Người dùng có thể thêm mới ghi chú, xem danh sách các ghi chú cũ và xóa các ghi chú không còn cần thiết.
* **Lưu trữ đám mây:** Toàn bộ dữ liệu được đồng bộ hóa và lưu trữ trên Google Firebase Firestore, đảm bảo dữ liệu luôn khả dụng.

## 3. Kiến Trúc Công Nghệ
* **Backend:** Xây dựng bằng **FastAPI** (Python), cung cấp các endpoint API chuẩn RESTful.
* **Frontend:** Xây dựng bằng **Streamlit**, tạo giao diện người dùng trực quan và phản hồi nhanh.
* **Database:** **Google Firestore** (Firebase) để lưu trữ dữ liệu theo thời gian thực.
* **Authentication:** **Firebase Auth** để quản lý phiên đăng nhập của người dùng.

## 4. Hướng Dẫn Cài Đặt

### Bước 1: Chuẩn bị môi trường
Yêu cầu máy tính đã cài đặt Python 3.10 trở lên.
1. Tải source code về máy và mở terminal tại thư mục gốc của dự án.
2. Tạo môi trường ảo:
   ```bash
   python -m venv venv
   ```
3. Kích hoạt môi trường ảo:
   * **Windows:** `.\venv\Scripts\activate`
   * **macOS/Linux:** `source venv/bin/activate`
4. Cài đặt các thư viện cần thiết:
   ```bash
   pip install -r requirements.txt
   ```

### Bước 2: Cấu hình Firebase (Bắt buộc)
Ứng dụng sử dụng file `secrets.toml` để lưu trữ các mã khóa bí mật. Bạn cần tạo thư mục `.streamlit` ở thư mục gốc và tạo file `secrets.toml` bên trong với cấu trúc sau:

```toml
[firebase_client]
apiKey="AI..."
authDomain="..."
databaseURL="..."
projectId="..."
storageBucket="..."
messagingSenderId="..."
appId="..."
measurementId="..."

[firebase_admin]
type="service_account"
project_id="..."
private_key_id="..."
private_key="-----BEGIN PRIVATE KEY-----..."
client_email="firebase-adminsdk-..."
client_id="..."
auth_uri="..."
token_uri="..."
auth_provider_x509_cert_url="..."
client_x509_cert_url="..."
universe_domain="..."
```

## 5. Hướng Dẫn Khởi Chạy Chương Trình

Để ứng dụng hoạt động, bạn cần chạy đồng thời cả Backend và Frontend trên hai terminal riêng biệt.

### Khởi động Backend (FastAPI)
Mở terminal thứ nhất và chạy lệnh:
```bash
python -m uvicorn backend.app.main:app --reload --port 8000
```
* API sẽ hoạt động tại: `http://localhost:8000`
* Kiểm tra trạng thái hệ thống tại: `http://localhost:8000/health`

### Khởi động Frontend (Streamlit)
Mở terminal thứ hai và chạy lệnh:
```bash
python -m streamlit run frontend/app.py
```
* Giao diện người dùng sẽ tự động mở tại: `http://localhost:8501`

## 6. Video Demo Sản Phẩm
Xem video hướng dẫn sử dụng và minh họa các tính năng của ứng dụng tại đường dẫn sau:
* **Link Video:** []

---
*Nguyễn Hữu Nhẩn - Khoa Công nghệ Thông tin - Trường Đại học Khoa học tự nhiên - ĐHQG TP.HCM.*