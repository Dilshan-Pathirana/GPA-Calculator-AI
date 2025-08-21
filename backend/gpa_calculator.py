from typing import List
from .grade_converter import GradeConverter
from models.course_model import Course

class GPACalculator:
    def __init__(self, converter: GradeConverter):
        self.converter = converter
        # Define weights by year: 1***/2*** = 20%, 3***/4*** = 30%
        self.year_weights = {1: 0.2, 2: 0.2, 3: 0.3, 4: 0.3}

    def calculate_weighted_gpa(self, courses: List[Course]) -> float:
        total_points = 0.0
        total_credits = 0.0
        year_credits: dict[int, float] = {1:0, 2:0, 3:0, 4:0}
        year_points: dict[int, float] = {1:0, 2:0, 3:0, 4:0}

        for c in courses:
            if c.grade.upper() in ["PENDING", "P"]:
                continue
            gp = self.converter.grade_to_points(c.grade)
            year = self._get_year_from_code(c.code)
            year_points[year] += gp * c.credits
            year_credits[year] += c.credits

        # Apply year weights
        for y in year_points:
            if year_credits[y] > 0:
                total_points += (year_points[y] / year_credits[y]) * self.year_weights[y]
                total_credits += self.year_weights[y]

        if total_credits == 0:
            return 0.0
        return total_points / total_credits

    def calculate_semester_gpa(self, courses: List[Course]) -> float:
        # Simple GPA ignoring year weights
        total_points = 0.0
        total_credits = 0.0
        for c in courses:
            if c.grade.upper() in ["PENDING", "P"]:
                continue
            gp = self.converter.grade_to_points(c.grade)
            total_points += gp * c.credits
            total_credits += c.credits
        return total_points / total_credits if total_credits > 0 else 0.0
   
   
    def _get_year_from_code(self, code: str) -> int:
        # Extract digits from code
        digits = ''.join(filter(str.isdigit, code))
        if not digits:
            return 1  # default to 1st year if no digits
        first_digit = int(digits[0])
        return min(first_digit, 4)  # limit to 1-4
