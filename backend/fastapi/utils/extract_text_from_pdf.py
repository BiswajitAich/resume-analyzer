import pdfplumber
from utils.states import ResumeAnalyserState

def extract_text_from_pdf(state: ResumeAnalyserState) -> ResumeAnalyserState:
    try:
        with pdfplumber.open(state['file'].file) as pdf:
            first_page = pdf.pages[0]
            text = first_page.extract_text().strip() or ""

        if not text:
            state['file_empty'] = True
            state['resume_text'] = "[NO TEXT EXTRACTED]"
        else:
            state['resume_text'] = text
    except Exception as e:
        state['resume_text'] = f"[ERROR] Failed to parse PDF: {str(e)}"
    return state