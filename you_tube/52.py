#PySide6 da css bo'yicha ishlash
import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QHBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1 = QPushButton("Button 1")
        self.button2 = QPushButton("Button 2")
        self.button3 = QPushButton("Button 3")
        self.initUI()

    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                font-weight: bold;
                font-style: italic;
                font-family: Arial;
                padding: 15px 75px;
                margin: 25px;
                border-radius: 5px;
                border: 2px solid black;
        }
            QPushButton#button1{
                background-color: hsl(217, 100%, 62%);
        }
            QPushButton#button2{
                background-color: hsl(104, 100%, 62%);
        }
            QPushButton#button3{
                background-color: hsl(53, 100%, 60%);

        }
            QPushButton#button1:hover{
                background-color: hsl(217, 100%, 82%);
        }
            QPushButton#button2:hover{
                background-color: hsl(104, 100%, 82%);
        }
            QPushButton#button3:hover{
                background-color: hsl(53, 100%, 80%);

        }
        """)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
