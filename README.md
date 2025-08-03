# Resume Analyzer 🔍📄

A powerful AI-driven Resume Analyzer that helps job seekers evaluate their resumes against a specific job description. Built with **Next.js** (Frontend) and **FastAPI** (Backend), this project utilizes LLMs to provide detailed, context-aware feedback on resume quality, alignment, and relevance.

---

## 🧠 Features

- 🖼 Upload resume in PDF format  
- 🧾 Paste job description text  
- 🤖 AI-powered resume analysis using GROQ LLM API  
- 📊 Insightful feedback on skills, alignment, and improvements  
- ⚡ Fast and lightweight with a clean, modern UI  
- 🌐 Full-stack structure (Next.js frontend + FastAPI backend)

---

## 📁 Project Structure

```
root/
├── frontend/    # Next.js 15 App Directory with Lucide React
├── backend/     # FastAPI for resume analysis (Deployed via Render)
└── README.md
```

---

## 🚀 Getting Started

### 🧩 Prerequisites to Use

- A **single-page resume** in PDF format  
- A **Job Description (JD)** within **1000 characters**  
- A valid [GROQ API Key](https://console.groq.com/keys)

---

## ⚙️ Tech Stack

- **Frontend:** Next.js 15, Lucide Icons  
- **Backend:** FastAPI, Python, GROQ LLM API  
- **Deployment:** Vercel (Frontend) + Render (Backend)

---

## 📡 API Endpoint

Interactive Docs: [https://resume-analyzer-q2ps.onrender.com/docs](https://resume-analyzer-q2ps.onrender.com/docs)

### 🔄 Request

**POST** `/analyze_resume`  
**Body:** `multipart/form-data`

**Fields:**
- `file` – Resume file in PDF format  
- `jd_text` – Job description (plain text)  
- `groq_api_key` – Your GROQ API key  

---

## 📜 License

MIT © [Biswajit Aich](https://github.com/BiswajitAich)

---

## 🙌 Acknowledgements

- **GROQ** for their blazing fast LLM API  
- **Vercel** for seamless frontend deployment  
- **Render** for reliable free-tier backend hosting

---

## 🌟 Contribute

Feel free to **fork**, **star**, **raise issues**, or **open pull requests**.  
Let’s improve the job application experience using AI together!
