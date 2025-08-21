# backend/ai_assistant.py
import google.generativeai as genai
from config import GEMINI_API_KEY
from models.course_model import Course
import json

class AIAssistant:
    def __init__(self, model: str = "gemini-1.5-flash"):
        if GEMINI_API_KEY:
            genai.configure(api_key=GEMINI_API_KEY)
            self.model = genai.GenerativeModel(model_name=model)
        else:
            self.model = None

    def parse_courses_from_text(self, text: str) -> list[Course]:
        """Parse transcript text using AI into Course objects."""
        if not self.model:
            return []

        try:
            prompt = (
                "You are a GPA assistant. Extract courses from the following transcript text. "
                "Return JSON array, each item with: code, name, credits, grade. "
                "Include pending courses as 'Pending' grade.\n\n"
                f"Transcript:\n{text}"
            )

            response = self.model.generate_content(prompt)
            raw_text = response.text.strip()

            if raw_text.startswith("```"):
                raw_text = raw_text.split("```")[1]
                raw_text = raw_text.replace("json", "", 1).strip()

            data = json.loads(raw_text)

            return [
                Course(
                    id=None,
                    code=d.get("code"),
                    name=d.get("name"),
                    credits=float(d.get("credits", 0)),
                    grade=d.get("grade")
                )
                for d in data
            ]
        except Exception as e:
            print(f"Parse error: {e}")
            return []

    def suggest_gpa_strategy(self, courses: list[Course], target_gpa: float) -> str:
        """Suggest strategies for improving GPA, only using pending courses."""
        if not self.model:
            return "AI not configured."

        pending_courses = [c for c in courses if c.grade.lower() in ("pending", "p")]

        if not pending_courses:
            return "No pending courses to improve GPA."

        try:
            summary = ", ".join(f"{c.code} ({c.credits} credits)" for c in pending_courses)
            prompt = (
                "You are a GPA advisor. Focus ONLY on pending courses.\n"
                f"Pending courses: {summary}\n"
                f"Target GPA: {target_gpa}\n"
                "Suggest 5 actionable strategies to improve GPA. "
                "Be concise and friendly. Include weight/credit considerations.\n"
            )

            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"Error: {e}"
