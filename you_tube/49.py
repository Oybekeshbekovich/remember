#PySide6 checkboxes->Belgilash
import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QCheckBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Checkbox misoli")
        self.setGeometry(200, 200, 520, 300)

        # Checkbox yaratish
        self.checkbox = QCheckBox("Men roziman", self)
        self.checkbox.setGeometry(10, 0, 500, 100)  # x, y, width, height
        self.checkbox.setStyleSheet("font-size: 18px;"
                                    "font-family: sans-serif;"
                                    "background-color:#6087c4;"
                                    "border-radius:5px;")

        # Checkbox holati o'zgarganda ishlash
        self.checkbox.stateChanged.connect(self.on_checkbox_change)

    def on_checkbox_change(self, state):
        if self.checkbox.isChecked():
            print("Checkbox belgilandi ✅")
        else:
            print("Checkbox olib tashlandi ❌")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
