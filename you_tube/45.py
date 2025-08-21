#PyQt5->yangi oyna yasash text uchun
import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel
from PySide6.QtGui import QIcon, QFont, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Oynaning sarlavhasi
        self.setWindowTitle("Mening PyQt5 Dasturim")

        # Oynaning o‘lchami (kenglik, balandlik)
        self.resize(500, 300)

        # Oynaning pozitsiyasi ekranda (x, y, width, height)
        self.setGeometry(200, 200, 500, 300)
        self.setWindowIcon(QIcon('icon.jpg'))
        label = QLabel('Salom', self)
        self.setFont(QFont('Arial', 40))
        label.setGeometry(0, 0, 500, 200)
        label.setStyleSheet("background-color : #3a82bd;"
                            'border-radius : 20px;'
                            'border-style : solid;'
                            'font-weight: bold;'
                            'font-style: italic;'
                            'font-size: 20px;'
                            'color:#dff5e8;'
                            'text-align: center;'
                            'text-decoration: underline;')
        # label.setAlignment(Qt.AlignTop) #->vertikaliga tepaga joylaydi
        # label.setAlignment(Qt.AlignBottom) #->vertikaliga pastga joylaydi
        # label.setAlignment(Qt.AlignVCenter) #->vertikaliga markazga joylaydi

        # label.setAlignment(Qt.AlignLeft) #->gorizantaliga chapga joylaydi
        # label.setAlignment(Qt.AlignRight) #->gorizantaliga o'ngga joylaydi
        # label.setAlignment(Qt.AlignHCenter) #->gorizantaliga markazga joylaydi
        label.setAlignment(Qt.AlignCenter)  # ->gorizantalga ham vertikaliga ham markazga joylaydi

        self.show()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
