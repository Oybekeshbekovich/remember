#PyQt5->yangi oyna yasash rasm uchun
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QIcon, QFont, Qt, QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mening PyQt5 Dasturim")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(700, 300, 500, 500)
        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)

        pximap = QPixmap('icon.jpg')
        label.setPixmap(pximap)

        label.setScaledContents(True)

        label.setGeometry((self.width() - label.width()) // 2,
                          (self.height() - label.height()) // 2,
                          label.width(),
                          label.height())

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()