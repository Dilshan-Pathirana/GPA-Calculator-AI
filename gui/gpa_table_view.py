from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton
from backend.database import Database


class GPATableView(QWidget):
    def __init__(self, db: Database) -> None:
        super().__init__()
        self.db = db

        layout = QVBoxLayout(self)
        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(["ID", "Course", "Credits", "Grade"])
        self.btn_clear = QPushButton("Clear All")

        layout.addWidget(self.table)
        layout.addWidget(self.btn_clear)

        self.btn_clear.clicked.connect(self._clear_all)

    def refresh(self) -> None:
        courses = self.db.get_all_courses()
        self.table.setRowCount(len(courses))
        for row, c in enumerate(courses):
            self.table.setItem(row, 0, QTableWidgetItem(str(c.id)))
            self.table.setItem(row, 1, QTableWidgetItem(c.name))
            self.table.setItem(row, 2, QTableWidgetItem(str(c.credits)))
            self.table.setItem(row, 3, QTableWidgetItem(c.grade))

    def _clear_all(self) -> None:
        self.db.clear_all()
        self.refresh()
