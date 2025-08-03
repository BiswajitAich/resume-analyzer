"use server";

const analyzeResumeServerAction = async (formData: FormData) => {
  const isProd = process.env.NODE_ENV === "production";
  const apiUrl = isProd
    ? "https://resume-analyzer-q2ps.onrender.com/analyze_resume"
    : "http://127.0.0.1:8000/analyze_resume";
  try {
    console.log(apiUrl);
    
    const response = await fetch(apiUrl, {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(
        errorData.message || `HTTP error! status: ${response.status}`
      );
    }

    const data = await response.json();
    return { success: true, data };
  } catch (error: any) {
    return { success: false, error: error.message };
  }
};

export default analyzeResumeServerAction;
