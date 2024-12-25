from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QApplication, QWidget
import os, random, time, subprocess
from tugas1 import Ui_Form

class MainController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Define colors for dynamic changes (optional, can be removed if not used)
        self.colors = ["red", "green", "blue", "yellow", "purple"]

        # Mapping buttons to applications or actions
        self.button_applications = {
            self.ui.pushButton_1: "https://www.google.co.id",
            self.ui.pushButton_3: "https://gobattle.io/?activate=88900/41731eef0d6ad05f0c26fdb2424102070d07e0ad#!",
            self.ui.pushButton_4: "https://www.facebook.com",
            self.ui.pushButton_5: "https://www.instagram.com/reel/DDrI0USNR8f/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==",
            self.ui.pushButton_7: "https://www.twitch.tv",
            self.ui.pushButton_8: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        }

        # Connect signals to methods
        self.ui.random_text.clicked.connect(self.display_text)
        self.ui.progess.clicked.connect(self.load_progress_bar)

        for button in self.button_applications.keys():
            button.clicked.connect(self.open_applications)

    def display_text(self):
        """Displays a random text in the label."""
        texts = [
            "Keep pushing forward!",
            "Success is just around the corner.",
            "Believe in yourself!",
            "Dream big, work hard.",
            "Stay positive and focused.",
        ]
        random_text = random.choice(texts)
        random_color = random.choice(self.colors)
        self.ui.label.setText(f'<span style="color:{random_color}">{random_text}</span>')

    def load_progress_bar(self):
        """Simulates loading a progress bar with a random delay."""
        self.ui.label.setText('<span style="color:orange">Don\'t touch until full 100%!</span>')
        random_delay = random.uniform(0.01, 0.05)

        for i in range(101):
            time.sleep(random_delay)
            self.ui.progressBar.setValue(i)
            QApplication.processEvents()  # Keep UI responsive during the loop

        # Display random text with random color after loading
        self.display_text()

    def open_applications(self):
        """Handles opening applications or URLs based on the button pressed."""
        button_id = self.sender()

        if button_id in self.button_applications:
            target = self.button_applications[button_id]

            if target.startswith("http"):
                # Open URL in the default web browser
                os.system(f'start {target}')  # For Windows, replace with 'open' for macOS
            else:
                try:
                    # Open an application
                    subprocess.Popen(target)
                except FileNotFoundError:
                    self.ui.label.setText(f"Application '{target}' not found.")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_window = MainController()
    main_window.show()
    sys.exit(app.exec())
