# gui/ai_chat_box.py
from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Signal
from backend.ai_assistant import AIAssistant

class AIChatBox(QWidget):
    # Signals
    parseRequested = Signal(str)
    whatIfRequested = Signal(list, float)
    suggestButtonClicked = Signal()  # for "Get Suggestions"

    def __init__(self):
        super().__init__()

        self.ai = AIAssistant()

        # GUI elements
        self.layout = QVBoxLayout()

        # 1️⃣ Input area for transcript text
        self.input_label = QLabel("Paste transcript here:")
        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("Paste your transcript or grades here...")

        # 2️⃣ Button to parse text
        self.parse_button = QPushButton("Parse Courses")

        # 3️⃣ Button to get GPA suggestions
        self.suggest_button = QPushButton("Get GPA Suggestions")

        # 4️⃣ Output area for AI messages
        self.response_box = QTextEdit()
        self.response_box.setReadOnly(True)

        # Add widgets to layout
        self.layout.addWidget(self.input_label)
        self.layout.addWidget(self.input_text)
        self.layout.addWidget(self.parse_button)
        self.layout.addWidget(self.suggest_button)
        self.layout.addWidget(self.response_box)
        self.setLayout(self.layout)

        # Connect buttons
        self.parse_button.clicked.connect(self.on_parse_clicked)
        self.suggest_button.clicked.connect(self.on_suggest_clicked)

    def on_parse_clicked(self):
        text = self.input_text.toPlainText()
        if text.strip():
            self.parseRequested.emit(text)

    def on_suggest_clicked(self):
        self.suggestButtonClicked.emit()

    def append_bot_message(self, message: str):
        """Append AI response to the text box."""
        current_text = self.response_box.toPlainText()
        if current_text:
            self.response_box.append("\n\n")
        self.response_box.append(message)
