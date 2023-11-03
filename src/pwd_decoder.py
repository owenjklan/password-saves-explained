
import logging
from pathlib import Path

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QGraphicsScene, QGraphicsView, QVBoxLayout, QPushButton, \
    QTextEdit
from PyQt5 import QtCore

from src.character_entry_widget import PasswordEntry

logger = logging.getLogger("pwd_decoder")


class PasswordDecoder(QWidget):
    MAX_VALUE = 0x10  # 16
    LEVELS = {
        0x0000: 0,
        0x1234: 1,
        0x3456: 2,
    }

    def __init__(self, pwdEntryWidget: PasswordEntry, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.value = 0
        self.textBlob = QTextEdit()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.textBlob)
        self.pwdEntryWidget = pwdEntryWidget
        self.show()

    @QtCore.pyqtSlot()
    def updateDecoding(self) -> None:
        pwdValue = self.pwdEntryWidget.value

        logger.info("pwdValue = %s", pwdValue)

        level = (pwdValue & 0xFFFF0) >> 4
        updatedText = ""
        if level in self.LEVELS:
            updatedText += f"Level {self.LEVELS[level]} unlocked!\n"
        else:
            updatedText += f"Value read: 0x{pwdValue:04x}\n"

        gearNibble = pwdValue & 0xF

        if gearNibble & 1 << 3:
            updatedText += "Player has the Long Sword\n"
        if gearNibble & 1 << 2:
            updatedText += "Player has Long Bow\n"
        if gearNibble & 1 << 1:
            updatedText += "Player has a Healing Potion\n"

        self.textBlob.setText(updatedText)
