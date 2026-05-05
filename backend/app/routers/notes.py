from fastapi import APIRouter, Depends, HTTPException, Query
from backend.app.dependencies.auth import get_current_user
from backend.app.schemas.notes import NoteRequest
from backend.app.services.firestore_service import save_note, get_notes, delete_note

router = APIRouter(prefix="/notes", tags=["notes"])

@router.get("")
def fetch_notes(limit: int = Query(default=20, ge=1, le=50), user=Depends(get_current_user)):
    try:
        notes = get_notes(user["uid"], limit=limit)
        return notes
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("")
def create_note(payload: NoteRequest, user=Depends(get_current_user)):
    try:
        save_note(user["uid"], payload.content)
        return {"message": "Đã lưu ghi chú thành công"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{note_id}")
def delete_user_note(note_id: str, user=Depends(get_current_user)):
    try:
        delete_note(user["uid"], note_id)
        return {"message": "Đã xóa ghi chú thành công"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))