#!/usr/bin/env python3
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QHBoxLayout, QVBoxLayout, QGraphicsScene, \
    QGraphicsView, QSpacerItem, QSizePolicy
# Only needed for access to command line arguments
import sys

from src.player import Player
from src.state_editor import StateEditorWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Saves Explained")
        self.saveStateButton = QPushButton("&Save with Password")
        self.loadStateButton = QPushButton("&Load from Password")
        self.editStateButton = QPushButton("&Edit State")

        # self.editStateButton()
        # self.loadStateButton()
        # self.saveStateButton()

        self.mainHLayout = QHBoxLayout()
        self.mainButtonsVLayout = QVBoxLayout()
        self.playerWidget = Player()
        self.mainButtonsVLayout.addWidget(self.playerWidget)

        self.addHPButton = QPushButton("&Add 5HP")
        self.takeHPButton = QPushButton("&Take 5HP")
        self.mainButtonsVLayout.addWidget(self.addHPButton)
        self.mainButtonsVLayout.addWidget(self.takeHPButton)

        self.addHPButton.clicked.connect(self.playerWidget.hp.hit_points_changed)

        self.mainButtonsVLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.mainButtonsVLayout.addWidget(self.editStateButton)
        self.mainButtonsVLayout.addWidget(self.saveStateButton)
        self.mainButtonsVLayout.addWidget(self.loadStateButton)

        self.scene = QGraphicsScene(0, 0, 640, 480)
        self.view = QGraphicsView(self.scene)

        self.mainHLayout.addLayout(self.mainButtonsVLayout)
        self.mainHLayout.addWidget(self.view)
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainHLayout)
        self.setCentralWidget(self.mainWidget)

        # Load pixap
        backgroundImage = QPixmap("images/background.png")
        self.scene.addPixmap(backgroundImage)
        self.scene.update()

        self.stateEditor = StateEditorWidget()
        self.editStateButton.clicked.connect(self.stateEditor.show)

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
