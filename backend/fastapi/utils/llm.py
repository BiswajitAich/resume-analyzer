from langchain_groq import ChatGroq
from utils.states import ResumeAnalyserState
from utils.messages import message
import json


def llm_response(state: ResumeAnalyserState) -> ResumeAnalyserState:
    resume_text = state["resume_text"]
    jd_text = state["JD_text"]

    llm = ChatGroq(
        model="llama-3.3-70b-versatile", 
        temperature=0.3, max_tokens=1024, 
        api_key=state["groq_api_key"]
        )

    print("=============== message.format called =================")
    prompt = message.format(resume_text=resume_text, JD_text=jd_text)

    try:
        raw_response = llm.invoke(prompt)
        parsed = json.loads(raw_response.content.strip())

        state["match_score"] = parsed.get("match_score", -1)
        state["summary"] = parsed.get("summary", "")

        skill_match = parsed.get("skill_match", {})
        state["skill_match"] = {
            "matched": skill_match.get("matched", []),
            "missing": skill_match.get("missing", []),
            "match_percent": skill_match.get("match_percent", 0.0)
        }

        experience_alignment = parsed.get("experience_alignment", {})
        state["experience_alignment"] = {
            "jd_experience_required": experience_alignment.get("jd_experience_required", ""),
            "resume_experience_summary": experience_alignment.get("resume_experience_summary", ""),
            "alignment": experience_alignment.get("alignment", "Poor")
        }

        state["soft_skills_detected"] = parsed.get("soft_skills_detected", [])

        keywords_overlap = parsed.get("keywords_overlap", {})
        state["keywords_overlap"] = {
            "common_keywords": keywords_overlap.get("common_keywords", []),
            "missing_keywords": keywords_overlap.get("missing_keywords", [])
        }

        recommendations = parsed.get("recommendations", {})
        state["recommendations"] = {
            "skills_to_add": recommendations.get("skills_to_add", []),
            "certifications_to_consider": recommendations.get("certifications_to_consider", []),
            "resume_improvement_tips": recommendations.get("resume_improvement_tips", [])
        }

    except Exception as e:
        state["match_score"] = -1
        state["summary"] = "[ERROR] Could not generate summary."
        state["skill_match"] = {
            "matched": [],
            "missing": [],
            "match_percent": 0.0
        }
        state["experience_alignment"] = {
            "jd_experience_required": "",
            "resume_experience_summary": "",
            "alignment": "Poor"
        }
        state["soft_skills_detected"] = []
        state["keywords_overlap"] = {
            "common_keywords": [],
            "missing_keywords": []
        }
        state["recommendations"] = {
            "skills_to_add": [],
            "certifications_to_consider": [],
            "resume_improvement_tips": []
        }

        print(f"[ERROR] Failed to parse LLM response: {e}\nRaw: {raw_response.content}")

    return state
