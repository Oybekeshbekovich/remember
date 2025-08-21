#PyQt5->yangi oyna yasash bo'lish uchun
#Vertikaliga taxlaydi
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PySide6.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mening PyQt5 Dasturim")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(700, 300, 500, 500)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label_1 = QLabel('#1', self)
        label_2 = QLabel('#2', self)
        label_3 = QLabel('#3', self)
        label_4 = QLabel('#4', self)
        label_5 = QLabel('#5', self)

        label_1.setStyleSheet("background-color:blue;")
        label_2.setStyleSheet("background-color:yellow;")
        label_3.setStyleSheet("background-color:red;")
        label_4.setStyleSheet("background-color:green;")
        label_5.setStyleSheet("background-color:purple;")

        vbox = QVBoxLayout()
        vbox.addWidget(label_1)
        vbox.addWidget(label_2)
        vbox.addWidget(label_3)
        vbox.addWidget(label_4)
        vbox.addWidget(label_5)

        central_widget.setLayout(vbox)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
#Gorizantaliga taxlaydi
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PySide6.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mening PyQt5 Dasturim")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(700, 300, 500, 500)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label_1 = QLabel('#1', self)
        label_2 = QLabel('#2', self)
        label_3 = QLabel('#3', self)
        label_4 = QLabel('#4', self)
        label_5 = QLabel('#5', self)

        label_1.setStyleSheet("background-color:blue;")
        label_2.setStyleSheet("background-color:yellow;")
        label_3.setStyleSheet("background-color:red;")
        label_4.setStyleSheet("background-color:green;")
        label_5.setStyleSheet("background-color:purple;")

        hbox = QHBoxLayout()
        hbox.addWidget(label_1)
        hbox.addWidget(label_2)
        hbox.addWidget(label_3)
        hbox.addWidget(label_4)
        hbox.addWidget(label_5)

        central_widget.setLayout(hbox)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
#Siz hohlagan ketmaketlikda taxlaydi
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from PySide6.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mening PyQt5 Dasturim")
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setGeometry(700, 300, 500, 500)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label_1 = QLabel('#1', self)
        label_2 = QLabel('#2', self)
        label_3 = QLabel('#3', self)
        label_4 = QLabel('#4', self)
        label_5 = QLabel('#5', self)

        label_1.setStyleSheet("background-color:blue;")
        label_2.setStyleSheet("background-color:yellow;")
        label_3.setStyleSheet("background-color:red;")
        label_4.setStyleSheet("background-color:green;")
        label_5.setStyleSheet("background-color:purple;")

        grid = QGridLayout()
        grid.addWidget(label_1,0,0)
        grid.addWidget(label_2,0,1)
        grid.addWidget(label_3,1,2)
        grid.addWidget(label_4,1,3)
        grid.addWidget(label_5,2,4)

        central_widget.setLayout(grid)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
