# Pythonda secondametr yasash
import sys
from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QApplication, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import QTime, QTimer, Qt
from PySide6.QtGui import QIcon


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.timer = QTimer(self)
        self.setGeometry(150, 300, 400, 250)
        self.stop_button = QPushButton("Stop", self)
        self.start_button = QPushButton("Start", self)
        self.reset_button = QPushButton("Reset", self)
        self.time_label = QLabel("00:00:00.00", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stopwatch")
        self.setWindowIcon(QIcon("istockphoto-990758324-612x612.jpg"))

        vbox = QVBoxLayout()
        vbox.addWidget(self.stop_button)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.reset_button)
        vbox.addWidget(self.time_label)

        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)

        self.start_button.setObjectName('start_button')
        self.stop_button.setObjectName('stop_button')
        self.reset_button.setObjectName('reset_button')

        self.setStyleSheet("""
            QPushButton, QLabel {
                    padding: 20px;
                    font-weight: bold;
                    font-family: calibri;
                    border-radius: 5px;
                    color: #616975;
                }
            QPushButton {
                font-size: 50px;
                background-color: #de2837;
                color: #000000;
            }
            QLabel {
                font-size: 120px;
                background-color: hsl(206, 69%, 71%);
            }
            QPushButton#start_button {
                border: 5px solid black;
                background-color: hsl(124, 44%, 44%);
                }
            QPushButton#stop_button {
                border: 5px solid black;
                background-color: hsl(352, 79%, 40%);
                }
            QPushButton#reset_button {
                border: 5px solid black;
                background-color: hsl(180, 10%, 48%);
                }
            QPushButton#start_button:hover {
                border: 5px solid black;
                background-color: hsl(124, 44%, 65%);
                }
            QPushButton#stop_button:hover {
                border: 5px solid black;
                background-color: hsl(352, 79%, 65%);
                }
            QPushButton#reset_button:hover {
                border: 5px solid black;
                background-color: hsl(180, 10%, 65%);
                }
        """)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        hour = time.hour()
        minute = time.minute()
        second = time.second()
        msec = time.msec() // 10
        return f"{hour:02}:{minute:02}:{second:02}:{msec:02}"

    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())
