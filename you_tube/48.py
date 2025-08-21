#PySide6 da Button->tugma yasash
import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.button = QPushButton("Ishni bajarish", self)
        self.label = QLabel("Bajarilmadi", self)
        self.setWindowTitle("My Window")
        self.initUI()

    def initUI(self):
        # Tugma yaratish
        self.button.setGeometry(150, 200, 200, 100)  # x, y, width, height
        self.button.setStyleSheet("font-size: 18px;"
                                  "border-radius: 5px;"
                                  "background-color:#174fb0 ;")
        # Tugma bosilganda ishlaydigan funksiya
        self.button.clicked.connect(self.on_button_click)

        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 25px;"
                                 "font-weight: bold;"
                                 "background-color: #0000;")
        self.label.setAlignment(Qt.AlignCenter)

    def on_button_click(self):
        self.label.setText("Bajarildi!👍")
        self.button.setStyleSheet("background-color:#79869c ;")
        self.button.setText("OK✅")
        self.button.setDisabled(True)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()