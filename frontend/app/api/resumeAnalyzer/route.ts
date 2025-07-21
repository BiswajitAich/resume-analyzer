import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
  try {
    const formData = await req.formData();

    const file = formData.get("file") as File;
    const jd_text = formData.get("jd_text");
    const groq_api_key = formData.get("groq_api_key");

    const backendFormData = new FormData();
    backendFormData.append("file", file);
    backendFormData.append("jd_text", jd_text as string);
    backendFormData.append("groq_api_key", groq_api_key as string);

    const response = await fetch("https://resume-analyzer-q2ps.onrender.com/analyze_resume", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: backendFormData,
    });
    if (!response.ok) {
      const errorData = await response.json();
      return NextResponse.json(
        {
          error: errorData.error || "Failed to analyze resume",
          results: null,
        },
        { status: response.status }
      );
    }
    const result = await response.json();
    return NextResponse.json(
      {
        results: result,
        error: null,
      },
      { status: 200 }
    );
  } catch (error) {
    console.error("Error in POST handler:", error);
    return NextResponse.json(
      {
        error: "Internal server error",
        results: null,
      },
      { status: 500 }
    );
  }
}
