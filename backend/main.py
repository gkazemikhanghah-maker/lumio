from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import anthropic
from dotenv import load_dotenv
import os
import json

load_dotenv()

app = FastAPI(title="Lumio API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

claude = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


class AnalyzeRequest(BaseModel):
    job_title: str
    experience_level: Optional[str] = "All"
    work_type: Optional[str] = "All"
    country: Optional[str] = "US"
    max_jobs: Optional[int] = 20


def analyze_with_claude(job_title: str, experience_level: str, work_type: str, country: str):
    prompt = f"""You are a job market analyst with deep knowledge of the current job market.

Generate realistic, accurate job market intelligence for "{job_title}" roles.
Experience level filter: {experience_level}
Work type filter: {work_type}
Country: {country}

Return ONLY a valid JSON object with this exact structure (no markdown, no explanation):
{{
  "skills": [
    {{"name": "string", "percentage": number, "trend": "up|down|stable"}}
  ],
  "salary": {{
    "min": number,
    "max": number,
    "median": number,
    "currency": "USD"
  }},
  "companies": [
    {{"name": "string", "count": number, "industry": "string"}}
  ],
  "experience": {{
    "min": number,
    "max": number,
    "median": number
  }},
  "trends": [
    {{"skill": "string", "direction": "up|down", "change_pct": number}}
  ],
  "summary": "3-4 sentence market overview",
  "total_analyzed": number
}}

Rules:
- skills: top 10 most in-demand skills for this role with realistic % frequency (must be role-specific)
- salary: realistic USD salary range for this role and experience level
- companies: 8-10 real companies known for hiring this role
- trends: 5 skills that are rising or falling in demand
- summary: insightful market overview specific to this role
- total_analyzed: use a realistic number between 200-500
- All data must be specific to "{job_title}" — not generic"""

    message = claude.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}]
    )

    response_text = message.content[0].text.strip()
    if response_text.startswith("```"):
        response_text = response_text.split("```")[1]
        if response_text.startswith("json"):
            response_text = response_text[4:]
    return json.loads(response_text.strip())


@app.get("/")
def root():
    return {"status": "Lumio API running", "version": "1.0.0"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze")
def analyze(req: AnalyzeRequest):
    try:
        print(f"Analyzing market for: {req.job_title}")
        result = analyze_with_claude(
            req.job_title,
            req.experience_level,
            req.work_type,
            req.country
        )
        result["job_title"] = req.job_title
        result["filters"] = {
            "experience_level": req.experience_level,
            "work_type": req.work_type,
            "country": req.country,
        }
        return result

    except json.JSONDecodeError as e:
        raise HTTPException(status_code=500, detail=f"Failed to parse AI response: {str(e)}")
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/test")
def test_endpoint():
    return {"status": "ok", "message": "Use POST /analyze with a job_title"}
