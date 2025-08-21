#PySide6 da time ko'rsatadigan qilish
import sys

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import QTimer, QTime, Qt
from PySide6.QtGui import QFont, QFontDatabase,QIcon

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel("12:00:00",self)
        self.timer = QTimer(self)
        #self.setWindowIcon(QIcon('icon.jpg'))
        self.setWindowIcon(QIcon('istockphoto-990758324-612x612.jpg'))
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Digital Clock')
        self.setGeometry(300, 300, 250, 150)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 100px;"
                                      "color: hsl(53, 69%, 40%)")
        font_id=QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        font_family=QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family,150)
        self.time_label.setFont(my_font)
        self.timer.timeout.connect(self.update_time)
        self.timer.start()

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString('hh:mm:ss AP')
        self.time_label.setText(current_time)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec())
