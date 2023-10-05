import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFont
from windowM import WindowP

if __name__ == "__main__":
    app = QApplication(sys.argv)
    font = QFont("Montserrat", 12)
    app.setFont(font)
    win = WindowP()
    win.show()
    app.exec()
