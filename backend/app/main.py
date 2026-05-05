from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.routers.auth import router as auth_router
from backend.app.routers.notes import router as notes_router

app = FastAPI(title="Note App Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(notes_router)

@app.get("/")
def information():
    return {
        "app_name": "Personal Note App API",
        "description": "Backend xử lý dữ liệu cho ứng dụng Ghi chú cá nhân",
        "author": "Nguyễn Hữu Nhẩn",
        "student_id": "24120206",
        "project": "Bài thực hành số 2 - Tư duy tính toán"
    }

@app.get("/health")
def health():
    return {
        "status": "ok", 
        "message": "Server đang hoạt động bình thường"
    }