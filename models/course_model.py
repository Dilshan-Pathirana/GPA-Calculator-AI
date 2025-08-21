# models/course_model.py
from dataclasses import dataclass
from typing import Optional

@dataclass
class Course:
    id: Optional[int]
    code: str
    name: str
    credits: float
    grade: str

    @property
    def year(self) -> int:
        """Determine year based on course code (first digit)."""
        try:
            return int(self.code[0])
        except:
            return 0
