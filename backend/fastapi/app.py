from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
from utils.workflow import workflow
from utils.states import ResumeAnalyserState
from fastapi.responses import JSONResponse
import os
import traceback

app = FastAPI()


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    favicon_path = os.path.join(os.path.dirname(__file__), "static", "favicon.ico")
    return FileResponse(favicon_path)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Resume Analyser API", "status": "running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/about")
def about():
    return {
        "name": "Resume Analyser",
        "version": "1.0.0",
        "description": "An API for analyzing resumes using AI.",
        "author": "Biswajit Aich",
        "license": "MIT",
        "repository": "",
        "website": "",
    }


@app.post("/analyze_resume")
async def analyze_resume(
    file: UploadFile = File(
        ...,
        description="Upload a PDF resume file (single page preferred)",
        example="resume.pdf",
        media_type="application/pdf",
    ),
    jd_text: str = Form(
        ...,
        description="Job description text to match against the resume with text length less than 1000 characters",
        example="We are hiring a full-stack engineer with React and Node.js experience.",
    ),
    groq_api_key: str = Form(
        ...,
        description="Your Groq API key for LLM access",
        example="your-groq-api-key",
    ),
):
    try:

        if not file.filename.endswith(".pdf"):
            return JSONResponse(
                status_code=400,
                content={
                    "message": "[ERROR]: Invalid file type. Please upload a PDF file.",
                },
            )

        if len(jd_text) > 1000:
            return JSONResponse(
                status_code=400,
                content={
                    "message": "[ERROR]: Job description text is too long. Please limit it to 1000 characters.",
                },
            )

        initial_input: ResumeAnalyserState = {
            "groq_api_key": groq_api_key,
            "file": file,
            "file_empty": False,
            "resume_text": "",
            "JD_text": jd_text,
            "match_score": -1,
            "summary": "",
            "skill_match": {"matched": [], "missing": [], "match_percent": 0.0},
            "experience_alignment": {
                "jd_experience_required": "",
                "resume_experience_summary": "",
                "alignment": "Poor",
            },
            "soft_skills_detected": [],
            "keywords_overlap": {"common_keywords": [], "missing_keywords": []},
            "recommendations": {
                "skills_to_add": [],
                "certifications_to_consider": [],
                "resume_improvement_tips": [],
            },
        }

        print("============ workflow.invoked ==================")
        result:ResumeAnalyserState = workflow.invoke(initial_input)
        print("============ result ===================")
        print(result)
        return {
            "match_score": result['match_score'],
            "summary": result["summary"],
            "skill_match": {"matched": result["skill_match"]["matched"], "missing": result["skill_match"]["missing"], "match_percent": result["skill_match"]["match_percent"]},
            "experience_alignment": {
                "jd_experience_required": result["experience_alignment"]["jd_experience_required"],
                "resume_experience_summary": result["experience_alignment"]["resume_experience_summary"],
                "alignment": result["experience_alignment"]["alignment"],
            },
            "soft_skills_detected": result["soft_skills_detected"],
            "keywords_overlap": {"common_keywords": result["keywords_overlap"]["common_keywords"], "missing_keywords": result["keywords_overlap"]["missing_keywords"]},
            "recommendations": {
                "skills_to_add": result["recommendations"]["skills_to_add"],
                "certifications_to_consider": result["recommendations"]["certifications_to_consider"],
                "resume_improvement_tips": result["recommendations"]["resume_improvement_tips"],
            },
        }
    except Exception as e:
        traceback.print_exc() 
        return JSONResponse(
            status_code=500,
            content={
                "message": f"[ERROR]: {str(e)}",
            },
        )
