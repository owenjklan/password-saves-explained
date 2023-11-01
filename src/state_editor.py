from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit, QLabel, QProgressBar, QPushButton


class StateEditorWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Edit Game State Values")
        self.maxHitPoints = 20
        self.hitPoints = self.maxHitPoints
        self.saveButton = QPushButton("&Save State")

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.hpEntry = QLineEdit()
        self.layout.addWidget(QLabel("Hitpoints"), 0, 0)
        self.layout.addWidget(self.hpEntry, 0, 1)
        self.layout.addWidget(self.saveButton, 2, 1)

        self.saveButton.clicked.connect(self.hide)
