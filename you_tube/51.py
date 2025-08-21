#PySide6 ediline-> kirish va tugma
import sys

from PySide6.QtWidgets import QMainWindow, QApplication,QLineEdit,QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit",self)
        self.setGeometry(700,300,500,500)
        self.setWindowTitle("My Window")
        self.initUI()


    def initUI(self):
        self.line_edit.setPlaceholderText("Enter your name")
        self.line_edit.setGeometry(10,10,100,40)
        self.line_edit.setStyleSheet("font-size:25px"
                                     "font-family:Arial;")
        self.button.setGeometry(110,10,100,40)
        self.button.setStyleSheet("font-size:25px"
                                     "font-family:Arial;")
        self.button.clicked.connect(self.submit)

    def submit(self):
        text = self.line_edit.text()
        print(f"Salom {text}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
