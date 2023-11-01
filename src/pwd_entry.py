#!/usr/bin/env python3
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QHBoxLayout, QVBoxLayout, QGraphicsScene, \
    QGraphicsView, QSpacerItem, QSizePolicy
# Only needed for access to command line arguments
import sys

from src.character_entry_widget import PasswordCharacterEntry
from src.player import Player
from src.state_editor import StateEditorWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Saves Explained - Password Entry")
        self.pwdWidget = PasswordCharacterEntry()
        self.pwdWidget2 = PasswordCharacterEntry()

        self.mainHLayout = QHBoxLayout()

        # self.addHPButton.clicked.connect(self.playerWidget.hp.hit_points_changed)
        self.mainHLayout.setSpacing(0)
        self.mainHLayout.addWidget(self.pwdWidget)
        self.mainHLayout.addWidget(self.pwdWidget2)
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainHLayout)
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
