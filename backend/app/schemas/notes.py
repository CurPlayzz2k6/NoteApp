from pydantic import BaseModel

class NoteRequest(BaseModel):
    content: str

class NoteResponse(BaseModel):
    id: str
    content: str
    timestamp: str