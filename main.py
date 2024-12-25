import sys
from PyQt6.QtWidgets import QApplication
from kontrol import MainController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = MainController()
    controller.show()
    sys.exit(app.exec())
