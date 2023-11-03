#!/usr/bin/env python3
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QHBoxLayout, QVBoxLayout, QGraphicsScene, \
    QGraphicsView, QSpacerItem, QSizePolicy
# Only needed for access to command line arguments
import sys

from src.character_entry_widget import PasswordEntry
from src.pwd_decoder import PasswordDecoder


class MainWindow(QMainWindow):
    PWD_CHARS_COUNT = 5
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Saves Explained - Password Entry")
        self.pwdEntryWidget = PasswordEntry()
        self.decodeButton = QPushButton("&Decode Password")
        self.passwordDecoder = PasswordDecoder(pwdEntryWidget=self.pwdEntryWidget)
        self.decodeButton.clicked.connect(self.pwdEntryWidget.updateValue)
        self.decodeButton.clicked.connect(self.passwordDecoder.updateDecoding)
        self.mainHLayout = QHBoxLayout()
        self.mainVLayout = QVBoxLayout()
        # self.addHPButton.clicked.connect(self.playerWidget.hp.hit_points_changed)
        self.mainHLayout.setSpacing(0)
        self.mainVLayout.addWidget(self.pwdEntryWidget)
        # self.mainVLayout.addLayout(self.mainHLayout)
        self.mainVLayout.addWidget(self.decodeButton)
        self.mainVLayout.addWidget(self.passwordDecoder)
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainVLayout)
        self.setCentralWidget(self.mainWidget)
        self.show()


def main():
    app = QApplication(sys.argv)

    # Create a Qt widget, which will be our window.
    window = MainWindow()
    window.show()  # IMPORTANT!!!!! Windows are hidden by default.

    # Start the event loop.
    app.exec()


# Your application won't reach here until you exit and the event
# loop has stopped.
if __name__ == "__main__":
    main()
