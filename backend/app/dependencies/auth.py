from fastapi import Security, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from backend.app.core.firebase_config import verify_id_token

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Security(security)):
    """
    Hàm này được dùng như một Dependency trong FastAPI.
    Nó sẽ tự động trích xuất token từ header (Bearer Token),
    gửi lên Firebase để kiểm tra xem token còn hợp lệ không.
    """
    token = credentials.credentials
    try:
        decoded_token = verify_id_token(token)
        return decoded_token # Chứa uid, email của người dùng
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token không hợp lệ hoặc đã hết hạn. Vui lòng đăng nhập lại.",
            headers={"WWW-Authenticate": "Bearer"},
        )