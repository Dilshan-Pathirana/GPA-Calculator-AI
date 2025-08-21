from PySide6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QComboBox, QPushButton, QDoubleSpinBox
from PySide6.QtCore import Signal


class GPAInputForm(QWidget):
    addRequested = Signal(str, float, str)

    def __init__(self) -> None:
        super().__init__()
        layout = QHBoxLayout(self)

        self.course_name = QLineEdit(placeholderText="Course name")
        self.credits = QDoubleSpinBox()
        self.credits.setRange(0, 50)
        self.credits.setValue(3.0)

        self.grade = QComboBox()
        self.grade.addItems(["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"])

        self.btn_add = QPushButton("Add Course")
        layout.addWidget(self.course_name)
        layout.addWidget(self.credits)
        layout.addWidget(self.grade)
        layout.addWidget(self.btn_add)

        self.btn_add.clicked.connect(self._emit_add)

    def _emit_add(self) -> None:
        if self.course_name.text():
            self.addRequested.emit(
                self.course_name.text(), float(self.credits.value()), self.grade.currentText()
            )
            self.course_name.clear()
