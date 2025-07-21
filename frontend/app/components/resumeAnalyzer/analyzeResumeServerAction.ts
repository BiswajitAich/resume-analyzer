"use server";

const analyzeResumeServerAction = async (formData: FormData) => {

  try {
    const response = await fetch(
      "https://resume-analyzer-q2ps.onrender.com/analyze_resume",
      {
        method: "POST",
        body: formData,
      }
    );

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
