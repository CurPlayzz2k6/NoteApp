import os
import tomllib
import pyrebase
import firebase_admin
from firebase_admin import credentials, firestore, auth

def load_secrets():
    # Lấy đường dẫn file secrets.toml trong thư mục .streamlit ở thư mục gốc
    secrets_path = os.path.join(os.getcwd(), ".streamlit", "secrets.toml")
    
    if not os.path.exists(secrets_path):
        raise FileNotFoundError(f"Không tìm thấy file cấu hình tại {secrets_path}")
        
    with open(secrets_path, "rb") as f:
        return tomllib.load(f)

secrets = load_secrets()

def init_firebase_admin():
    if not firebase_admin._apps:
        admin_config = secrets.get("firebase_admin", {})
        
        # Xử lý format ký tự xuống dòng cho private_key
        if "private_key" in admin_config:
            admin_config["private_key"] = admin_config["private_key"].replace("\\n", "\n")
            
        cred = credentials.Certificate(admin_config)
        firebase_admin.initialize_app(cred)

def get_firestore():
    init_firebase_admin()
    return firestore.client()

def get_pyrebase_auth():
    client_config = secrets.get("firebase_client", {})
    firebase = pyrebase.initialize_app(client_config)
    return firebase.auth()

def verify_id_token(id_token: str):
    init_firebase_admin()
    return auth.verify_id_token(id_token)