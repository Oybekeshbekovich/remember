#PySide6 da radio buttons
import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QRadioButton, QButtonGroup


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.button_gproup1 = QButtonGroup()
        self.button_gproup2 = QButtonGroup()
        self.setWindowTitle("RadioButton misoli")
        self.setGeometry(200, 200, 400, 300)
        # Radio tugmalar yaratish
        self.radio1 = QRadioButton("Visa", self)
        self.radio1.setGeometry(10, 0, 100, 30)

        self.radio2 = QRadioButton("MasterCard", self)
        self.radio2.setGeometry(10, 50, 100, 30)
        self.radio3 = QRadioButton("Humo", self)
        self.radio3.setGeometry(10, 100, 100, 30)
        self.radio4 = QRadioButton("In-Store", self)
        self.radio4.setGeometry(10, 150, 100, 30)
        self.radio5 = QRadioButton("Online", self)
        self.radio5.setGeometry(10, 200, 100, 30)

        self.button_gproup1.addButton(self.radio1)
        self.button_gproup1.addButton(self.radio2)
        self.button_gproup1.addButton(self.radio3)
        self.button_gproup2.addButton(self.radio4)
        self.button_gproup2.addButton(self.radio5)

        # Birinchi tugma default tanlangan bo‘lsin
        # self.radio1.setChecked(False)
        # self.radio2.setChecked(False)
        # self.radio3.setChecked(False)
        # self.radio4.setChecked(False)
        # self.radio5.setChecked(False)

        # Hodisa ulash
        self.radio1.toggled.connect(self.on_radio_change)
        self.radio2.toggled.connect(self.on_radio_change)
        self.radio3.toggled.connect(self.on_radio_change)
        self.radio4.toggled.connect(self.on_radio_change)
        self.radio5.toggled.connect(self.on_radio_change)

    def on_radio_change(self):
        if self.radio1.isChecked():
            print(f"Tanlov {self.radio1.text()} ✅")
        elif self.radio2.isChecked():
            print(f"Tanlov {self.radio2.text()} ✅")
        elif self.radio3.isChecked():
            print(f"Tanlov {self.radio3.text()} ✅")
        elif self.radio4.isChecked():
            print(f"Tanlov {self.radio4.text()} ✅")
        elif self.radio5.isChecked():
            print(f"Tanlov {self.radio5.text()} ✅")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
