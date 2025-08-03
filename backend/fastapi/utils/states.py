from fastapi import UploadFile
from typing import TypedDict, List

class SkillMatch(TypedDict):
    matched: List[str]
    missing: List[str]
    match_percent: float

class ExperienceAlignment(TypedDict):
    jd_experience_required: str
    resume_experience_summary: str
    alignment: str  

class KeywordsOverlap(TypedDict):
    common_keywords: List[str]
    missing_keywords: List[str]

class Recommendations(TypedDict):
    skills_to_add: List[str]
    certifications_to_consider: List[str]
    resume_improvement_tips: List[str]

class ResumeAnalyserState(TypedDict):
    groq_api_key: str
    file: UploadFile
    file_empty: bool
    resume_text: str
    JD_text: str
    match_score: float 
    summary: str
    skill_match: SkillMatch
    experience_alignment: ExperienceAlignment
    soft_skills_detected: List[str]
    keywords_overlap: KeywordsOverlap
    recommendations: Recommendations
