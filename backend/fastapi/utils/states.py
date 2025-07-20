from typing import TypedDict
from fastapi import UploadFile

class ResumeAnalyserState(TypedDict):
    groq_api_key: str
    file: UploadFile
    file_empty: bool
    resume_text: str
    JD_text: str
    resume_rating: float
    resume_jd_match: float
    analysis: str