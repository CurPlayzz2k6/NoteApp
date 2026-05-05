from datetime import datetime, timezone
from backend.app.core.firebase_config import get_firestore
from firebase_admin import firestore

db = get_firestore()

def save_note(uid: str, content: str):
    doc = {
        "content": content,
        "ts": datetime.now(timezone.utc)
    }
    # Lưu note vào collection riêng của từng user
    db.collection("users").document(uid).collection("notes").add(doc)

def get_notes(uid: str, limit: int = 20):
    q = (
        db.collection("users")
        .document(uid)
        .collection("notes")
        .order_by("ts", direction=firestore.Query.DESCENDING)
        .limit(limit)
    )
    docs = list(q.stream())
    
    return [
        {
            "id": d.id,
            "content": d.to_dict().get("content", ""),
            "timestamp": d.to_dict().get("ts").strftime("%d/%m/%Y %H:%M") if d.to_dict().get("ts") else ""
        }
        for d in docs
    ]

def delete_note(uid: str, note_id: str):
    # Trỏ chính xác đến document (ghi chú) cần xóa thông qua note_id
    db.collection("users").document(uid).collection("notes").document(note_id).delete()