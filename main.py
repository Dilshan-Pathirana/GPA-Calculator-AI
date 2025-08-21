import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from config import ASSETS_DIR
from gui.main_window import MainWindow


def main() -> None:
    app = QApplication(sys.argv)
    app.setApplicationName("GPA Calculator")
    app.setOrganizationName("MyOrg")

    icon_path = ASSETS_DIR / "logo.png"
    if icon_path.exists():
        app.setWindowIcon(QIcon(str(icon_path)))

    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
