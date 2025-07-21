"use client";
import React, { useState, ChangeEvent, DragEvent } from "react";
import { Upload, FileText, Zap, CheckCircle, AlertCircle } from "lucide-react";
import styles from "./ResumeAnalyzer.module.css";
import analyzeResumeServerAction from "./analyzeResumeServerAction";

interface AnalysisResults {
  resume_rating: number;
  resume_jd_match: number;
  analysis: string;
}

export default function ResumeAnalyzer() {
  const [file, setFile] = useState<File | null>(null);
  const [jobDescription, setJobDescription] = useState<string>("");
  const [apiKey, setApiKey] = useState<string>("");
  const [results, setResults] = useState<AnalysisResults | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const [dragActive, setDragActive] = useState<boolean>(false);

  const handleDrag = (e: DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === "dragenter" || e.type === "dragover") setDragActive(true);
    else if (e.type === "dragleave") setDragActive(false);
  };

  const handleDrop = (e: DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      const droppedFile = e.dataTransfer.files[0];
      if (droppedFile.type === "application/pdf") {
        setFile(droppedFile);
        setError(null);
      } else {
        setError("Please upload a PDF file only.");
      }
    }
  };

  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      const selectedFile = e.target.files[0];
      if (selectedFile.type === "application/pdf") {
        setFile(selectedFile);
        setError(null);
      } else {
        setError("Please upload a PDF file only.");
      }
    }
  };

const handleSubmit = async () => {
  if (!file || !jobDescription.trim() || !apiKey.trim()) {
    setError("Please fill in all fields and upload a resume.");
    return;
  }

  setLoading(true);
  setError(null);
  setResults(null);

  const formData = new FormData();
  formData.append("file", file);
  formData.append("jd_text", jobDescription);
  formData.append("groq_api_key", apiKey);

  try {
    const result = await analyzeResumeServerAction(formData);
    
    if (!result.success) {
      throw new Error(result.error);
    }

    setResults(result.data);
  } catch (err: any) {
    setError(`Analysis failed: ${err.message}`);
  } finally {
    setLoading(false);
  }
};

  const getRatingColor = (rating: number) => {
    if (rating >= 4) return "#10b981";
    if (rating >= 3) return "#f59e0b";
    return "#ef4444";
  };

  const getMatchColor = (match: number) => {
    if (match >= 0.7) return "#10b981";
    if (match >= 0.5) return "#f59e0b";
    return "#ef4444";
  };

  const isFormValid =
    file && jobDescription.trim() && apiKey.trim() && !loading;

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <h1 className={styles.title}>Resume Analyzer</h1>
        <p className={styles.subtitle}>
          Get AI-powered insights on how well your resume matches job
          requirements
        </p>
      </div>

      <div className={styles.mainContent}>
        <div className={styles.card}>
          <div className={styles.formContainer}>
            <div className={styles.formGroup}>
              <label className={styles.label}>Upload Resume (PDF)</label>
              <div
                className={`${styles.fileUpload} ${
                  dragActive ? styles.fileUploadActive : ""
                }`}
                onDragEnter={handleDrag}
                onDragLeave={handleDrag}
                onDragOver={handleDrag}
                onDrop={handleDrop}
                onClick={() => document.getElementById("fileInput")?.click()}
              >
                <div className={styles.fileUploadContent}>
                  <Upload size={24} color="#6366f1" />
                  <p>
                    {file
                      ? file.name
                      : "Drag and drop your resume here, or click to browse"}
                  </p>
                  <p style={{ fontSize: "0.875rem", color: "#9ca3af" }}>
                    PDF files only, (single page resumes)
                  </p>
                </div>
                <input
                  id="fileInput"
                  type="file"
                  accept=".pdf"
                  onChange={handleFileChange}
                  style={{ display: "none" }}
                />
              </div>
            </div>

            <div className={styles.formGroup}>
              <label className={styles.label}>Job Description</label>
              <textarea
                className={styles.textarea}
                value={jobDescription}
                onChange={(e) => setJobDescription(e.target.value)}
                placeholder="Paste the job description here (max 1000 characters)..."
                maxLength={1000}
              />
              <div className={styles.characterCount}>
                {jobDescription.length}/1000 characters
              </div>
            </div>

            <div className={styles.formGroup}>
              <label className={styles.label}>Groq API Key</label>
              <input
                type="password"
                className={styles.input}
                value={apiKey}
                onChange={(e) => setApiKey(e.target.value)}
                placeholder="Enter your Groq API key"
              />
            </div>

            <button
              onClick={handleSubmit}
              disabled={!isFormValid}
              className={`${styles.button} ${styles.buttonPrimary} ${
                !isFormValid ? styles.buttonDisabled : ""
              }`}
            >
              {loading ? (
                <>
                  <div className={styles.spinner}></div>
                  Analyzing...
                </>
              ) : (
                <>
                  <Zap size={20} />
                  Analyze Resume
                </>
              )}
            </button>
          </div>
        </div>

        {error && (
          <div className={styles.errorCard}>
            <div className={styles.errorHeader}>
              <AlertCircle size={20} />
              <strong>Error</strong>
            </div>
            <p>{error}</p>
          </div>
        )}

        {results && (
          <div className={styles.resultsCard}>
            <div className={styles.resultsHeader}>
              <CheckCircle size={24} />
              <h2>Analysis Results</h2>
            </div>

            <div className={styles.metricsGrid}>
              <div className={styles.metricCard}>
                <div
                  className={styles.metricValue}
                  style={{ color: getRatingColor(results.resume_rating) }}
                >
                  {results.resume_rating}/5
                </div>
                <div className={styles.metricLabel}>Resume Rating</div>
              </div>

              <div className={styles.metricCard}>
                <div
                  className={styles.metricValue}
                  style={{ color: getMatchColor(results.resume_jd_match) }}
                >
                  {Math.round(results.resume_jd_match * 100)}%
                </div>
                <div className={styles.metricLabel}>Job Match Score</div>
              </div>
            </div>

            <div className={styles.analysisSection}>
              <h3 className={styles.analysisTitle}>
                <FileText size={20} />
                Detailed Analysis
              </h3>
              <p>{results.analysis}</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
