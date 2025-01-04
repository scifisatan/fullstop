from pydantic import BaseModel
from pydantic import Enum, Optional, List, Dict

class ChatRequest(BaseModel):
    mode: Enum["text", "voice"]
    user_input: Optional[str] = None
    history: List[Dict[str, str]] = []

class ChatResponse(BaseModel):
    answer: str


class TTSRequest(BaseModel):
    text: str

class TTSResponse(BaseModel):
    message: str
    audio_url: Optional[str] = None

class STTResponse(BaseModel):
    text: str
    message: str