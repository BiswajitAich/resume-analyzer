import styles from "./page.module.css";
import ResumeAnalyzer from "./components/resumeAnalyzer/ResumeAnalyzer";
import { Github, Linkedin } from "lucide-react";
import Link from "next/link";

export default function Home() {
  return (
    <div className={styles.page}>
      <main className={styles.main}>
        <ResumeAnalyzer />
      </main>
      <footer className={styles.footer}>
        <span>© {new Date().getFullYear()} Resume Analyzer</span>
        <Link
          href="https://github.com/BiswajitAich/resume-analyzer"
          target="_blank"
          rel="noopener noreferrer"
        >
          <Github />
          GitHub
        </Link>
        <Link
          href="https://www.linkedin.com/in/biswajitaich"
          target="_blank"
          rel="noopener noreferrer"
        >
          <Linkedin />
          LinkedIn
        </Link>
      </footer>
    </div>
  );
}
