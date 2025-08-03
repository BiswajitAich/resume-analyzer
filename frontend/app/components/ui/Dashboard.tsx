import { AnalysisResults } from "../types/analysisResults";
import styles from "./dashBoard.module.css";

const Dashboard = ({ data }: { data: AnalysisResults }) => {
  return (
    <div className={styles.dashboardContainer}>
      <h1 className={styles.header}>Resume Analysis Summary</h1>

      <section className={styles.card}>
        <h2 className={styles.title}>
          Match Score
          <div className={styles.circleContainer}>
            <div
              className={styles.circle}
              style={{ "--score": data.match_score } as React.CSSProperties}
            >
              <span>{data.match_score}%</span>
            </div>
          </div>
        </h2>

        <p className={styles.summary}>{data.summary}</p>
      </section>

      <section className={styles.flexSection}>
        <div className={styles.card}>
          <h2 className={styles.title}>Skill Match</h2>
          <table className={styles.table}>
            <thead>
              <tr>
                <th>
                  <strong>Matched</strong>
                </th>
                <th>
                  <strong>Missing</strong>
                </th>
              </tr>
            </thead>
            <tbody>
              {Array.from({
                length: Math.max(
                  data.skill_match.matched.length,
                  data.skill_match.missing.length
                ),
              }).map((_, idx) => (
                <tr key={idx}>
                  <td>{data.skill_match.matched[idx] || ""}</td>
                  <td>{data.skill_match.missing[idx] || ""}</td>
                </tr>
              ))}
            </tbody>
          </table>
          <p>
            <strong>Match %:</strong>
            <div
              className={styles.match}
              style={
                {
                  "--match": data.skill_match.match_percent,
                } as React.CSSProperties
              }
            >
              {data.skill_match.match_percent}%
            </div>
          </p>
        </div>

        <div className={styles.card}>
          <h2 className={styles.title}>Experience Alignment</h2>
          <p>
            <strong>Required:</strong>{" "}
            {data.experience_alignment.jd_experience_required}
          </p>
          <p>
            <strong>Resume:</strong>{" "}
            {data.experience_alignment.resume_experience_summary}
          </p>
          <p>
            <strong>Alignment:</strong> {data.experience_alignment.alignment}
          </p>
        </div>
      </section>

      <section className={styles.card}>
        <h2 className={styles.title}>Soft Skills Detected</h2>
        <ul className={styles.ul}>
          {data.soft_skills_detected.map((skill, idx) => (
            <li key={idx}>{skill}</li>
          ))}
        </ul>
      </section>

      <section className={styles.flexSection}>
        <div className={styles.card}>
          <h2 className={styles.title}>Keyword Overlap</h2>
          <p>
            <strong>Common:</strong>{" "}
            {data.keywords_overlap.common_keywords.join(", ")}
          </p>
          <p>
            <strong>Missing:</strong>{" "}
            {data.keywords_overlap.missing_keywords.join(", ")}
          </p>
        </div>

        <div className={styles.card}>
          <h2 className={styles.title}>Recommendations</h2>
          <p>
            <strong>Skills to Add:</strong>{" "}
            {data.recommendations.skills_to_add.join(", ")}
          </p>
          <p>
            <strong>Certifications:</strong>{" "}
            {data.recommendations.certifications_to_consider.join(", ")}
          </p>
          <p>
            <strong>Resume Tips:</strong>{" "}
            {data.recommendations.resume_improvement_tips.join(", ")}
          </p>
        </div>
      </section>
    </div>
  );
};

export default Dashboard;
