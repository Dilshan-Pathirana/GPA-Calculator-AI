from config import DEFAULT_GPA_SCALE


class GradeConverter:
    # Map letter grades to points
    grade_map = {
        "A+": 4.0,
        "A": 4.0,
        "A-": 3.7,
        "B+": 3.3,
        "B": 3.0,
        "B-": 2.7,
        "C+": 2.3,
        "C": 2.0,
        "C-": 1.7,
        "D+": 1.3,
        "D": 1.0,
        "F": 0.0,
        "P": 0.0,      # Pass (ignored in weighted GPA)
        "Pending": 0.0 # Pending (ignored)
    }

    def grade_to_points(self, grade: str) -> float:
        return self.grade_map.get(grade.upper(), 0.0)
