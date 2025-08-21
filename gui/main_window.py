# gui/main_window.py
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QSplitter, QLabel
from PySide6.QtCore import Qt
from .gpa_input_form import GPAInputForm
from .gpa_table_view import GPATableView
from .ai_chat_box import AIChatBox
from backend.gpa_calculator import GPACalculator
from backend.grade_converter import GradeConverter
from backend.database import Database

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("GPA Calculator")
        self.resize(1200, 750)

        # Backend
        self.db = Database()
        self.converter = GradeConverter()
        self.calculator = GPACalculator(self.converter)

        # GUI widgets
        self.input_form = GPAInputForm()
        self.table_view = GPATableView(self.db)
        self.ai_chat = AIChatBox()

        # Layout
        center = QWidget()
        layout = QVBoxLayout(center)
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.table_view)
        splitter.addWidget(self.ai_chat)

        layout.addWidget(self.input_form)
        layout.addWidget(splitter)
        self.setCentralWidget(center)

        # Connect signals
        self.input_form.addRequested.connect(self._on_add_course)
        self.ai_chat.parseRequested.connect(self._on_parse_text)
        self.ai_chat.suggestButtonClicked.connect(self._on_suggest_ai)

        self.table_view.refresh()
        self.update_total_gpa()

    def _on_add_course(self, code: str, name: str, credits: float, grade: str) -> None:
        self.db.add_course(code, name, credits, grade)
        self.table_view.refresh()
        self.update_total_gpa()

    def _on_parse_text(self, text: str) -> None:
        from backend.ai_assistant import AIAssistant
        ai = AIAssistant()
        courses = ai.parse_courses_from_text(text)
        for c in courses:
            self.db.add_course(c.code, c.name, c.credits, c.grade)
        self.table_view.refresh()
        self.update_total_gpa()

    def _on_suggest_ai(self) -> None:
        from backend.ai_assistant import AIAssistant
        ai = AIAssistant()
        advice = ai.suggest_gpa_strategy(self.db.get_all_courses(), target_gpa=3.8)
        self.ai_chat.append_bot_message(advice)

    def update_total_gpa(self):
        courses = self.db.get_all_courses()
        gpa = self.calculator.calculate_weighted_gpa(courses)
        self.statusBar().showMessage(f"Current Weighted GPA: {gpa:.2f}")
