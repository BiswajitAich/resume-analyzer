from fastapi import FastAPI, UploadFile, File, Form
from fastapi.staticfiles import StaticFiles
from utils.workflow import workflow
from fastapi.responses import JSONResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

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
        "website": ""
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
        example="We are hiring a full-stack engineer with React and Node.js experience."
        ),
    groq_api_key: str = Form(
        ...,
        description="Your Groq API key for LLM access",
        example="your-groq-api-key",
        )
    ):
    try:

        if not file.filename.endswith('.pdf'):
            return JSONResponse(
                status_code=400, 
                content={
                    "message": "Invalid file type. Please upload a PDF file.",
                    "resume_rating": -1,
                    "resume_jd_match": -1,
                    "analysis": "[ERROR] Invalid file type."
                }
            )

        if len(jd_text) > 1000:
            return JSONResponse(
                status_code=400, 
                content={
                    "message": "Job description text is too long. Please limit it to 1000 characters.",
                    "resume_rating": -1,
                    "resume_jd_match": -1,
                    "analysis": "[ERROR] Job description text is too long."
                }
            )

        initial_input = {
            "groq_api_key": groq_api_key,
            "file_empty": False,
            "file": file,
            "JD_text": jd_text,
            "resume_rating": -1,
            "resume_jd_match": -1,
            "analysis": "No analysis done yet.",
        }
        result = workflow.invoke(initial_input)
        return {
            "resume_rating": result['resume_rating'],
            "resume_jd_match": result['resume_jd_match'],
            "analysis": result['analysis']
        }
    except Exception as e:
        return JSONResponse(
            status_code=500, 
            content={
            "resume_rating": -1,
            "resume_jd_match": -1,
            "analysis": f"[ERROR] An error occurred during analysis: {str(e)}",
            "message": "Please check the input file and try again."
        })