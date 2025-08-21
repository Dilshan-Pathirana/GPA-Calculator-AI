from backend.ai_assistant import AIAssistant
from models.course_model import Course

def main():
    # Initialize AI assistant
    ai = AIAssistant()

    # Hardcoded course list (sample from your transcript)
    courses = [
        Course(id=None, name="Cell Biology and Genetics", credits=2, grade="A"),
        Course(id=None, name="Basic Ecology", credits=2, grade="A-"),
        Course(id=None, name="Biomolecules and Their Applications", credits=2, grade="B-"),
        Course(id=None, name="Principles of Chemistry I", credits=3, grade="B"),
        Course(id=None, name="Elementary Chemistry Laboratory I", credits=1, grade="A"),
        Course(id=None, name="Computer Applications", credits=2, grade="A"),
        Course(id=None, name="Industrial Placement", credits=8, grade="Pending"),
        Course(id=None, name="Research Methodology & Scientific Writing", credits=2, grade="Pending"),
        Course(id=None, name="Seminar", credits=1, grade="Pending"),
    ]

    # 1️⃣ Display the hardcoded courses
    print("=== Hardcoded Courses ===")
    for c in courses:
        print(f"{c.name}: {c.grade} ({c.credits} credits)")

    # 2️⃣ Test AI suggest_gpa_strategy
    target_gpa = 3.8
    print("\n=== Testing AI GPA Strategy Suggestions ===")
    advice = ai.suggest_gpa_strategy(courses, target_gpa)
    print(advice)


if __name__ == "__main__":
    main()
