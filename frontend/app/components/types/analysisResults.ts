export interface AnalysisResults {
  match_score: number,
  summary: string,
  skill_match: {
    matched: string[],
    missing: string[],
    match_percent: number
  },
  experience_alignment: {
    jd_experience_required: string,
    resume_experience_summary: string,
    alignment: string
  },
  soft_skills_detected: string[],
  keywords_overlap: {
    common_keywords: string[],
    missing_keywords: string[]
  },
  recommendations: {
    skills_to_add: string[],
    certifications_to_consider: string[],
    resume_improvement_tips: string[]
  }
}