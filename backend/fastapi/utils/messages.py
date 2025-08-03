message = """You are a professional job matching assistant. 

Below is a candidate's resume and a job description. Your task is to analyze the two and extract structured insights in **valid JSON** for dashboard rendering. 
Write precisely and professionally ( max 200 words in sentense key and 10 words in each list key ) maintaining vaild json format no markdown('''json...''').
---
📄 Resume: {resume_text} 

---
📋 Job Description: {JD_text} 

---
🎯 Your task: Analyze the resume and JD and output the following as valid JSON: 

{{
  "match_score": float (0 to 100),   
  "summary": string,   
  "skill_match": {{
    "matched": [list of strings],
    "missing": [list of strings],
    "match_percent": float (0 to 100)
  }},
  "experience_alignment": {{
    "jd_experience_required": string,
    "resume_experience_summary": string,
    "alignment": string ("Excellent" | "Good" | "Partial" | "Poor")
  }},
  "soft_skills_detected": [list of strings],
  "keywords_overlap": {{
    "common_keywords": [list of strings],
    "missing_keywords": [list of strings]
  }},
  "recommendations": {{
    "skills_to_add": [list of strings],
    "certifications_to_consider": [list of strings],
    "resume_improvement_tips": [list of strings]
  }}
}}

Only return valid JSON. Do not add commentary or any explanation."""