from langchain_groq import ChatGroq
from utils.states import ResumeAnalyserState
from utils.messages import message
import json


def llm_response(state: ResumeAnalyserState) -> ResumeAnalyserState:
    resume_text = state["resume_text"]
    jd_text = state["JD_text"]

    llm = ChatGroq(
        model="llama-3.3-70b-versatile", 
        temperature=1.0, max_tokens=1024, 
        api_key=state["groq_api_key"]
        )

    prompt = message.format(resume_text=resume_text, JD_text=jd_text)
    response = llm.invoke(prompt)

    try:
        parsed = json.loads(response.content.strip())
        state["resume_rating"] = parsed.get("resume_rating", -1)
        state["resume_jd_match"] = parsed.get("resume_jd_match", -1.0)
        state["analysis"] = parsed.get("analysis", "No analysis provided.")
    except Exception as e:
        state["resume_rating"] = -1
        state["resume_jd_match"] = -1
        state["analysis"] = (
            f"[ERROR] Failed to parse LLM response: {str(e)}\nRaw: {response.content}"
        )

    return state
