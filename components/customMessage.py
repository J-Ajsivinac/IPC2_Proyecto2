from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QIcon


class MsgBox(QMessageBox):
    def __init__(self, title, text):
        super().__init__()
        self.setWindowTitle(title)
        self.setText(text)

    def set_custom_icon(self, icon):
        self.setIconPixmap(icon)
        q_icon = QIcon(icon)
        self.setWindowIcon(q_icon)


def correct_msgbox(title, text):
    msg_box = MsgBox(title, text)
    msg_box.exec()


def error_msgbox(title, text):
    msg_box = MsgBox(title, text)
    msg_box.exec()


def alert_msgbox(title, text):
    msg_box = MsgBox(title, text)
    msg_box.exec()
