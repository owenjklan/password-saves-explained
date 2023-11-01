from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit, QLabel, QProgressBar


class HitPointsDisplay(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.maxHitPoints = 20
        self.hitPoints = self.maxHitPoints

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.hitPointsLabel = QLabel(f"{self.hitPoints}/{self.maxHitPoints}")

        self.layout.addWidget(QLabel("HP"), 0, 0)
        self.layout.addWidget(self.hitPointsLabel, 0, 1)
        self.progress = QProgressBar()
        self.progress.setRange(0, self.maxHitPoints)
        self.progress.setValue(self.hitPoints)
        self.progress.show()
        self.layout.addWidget(self.progress, 1, 0, 1, 2)

    @QtCore.pyqtSlot()
    def hit_points_changed(self):
        self.hitPoints += self.parentWidget().hitPoints
        self.progress.setValue(self.hitPoints)
        self.hitPointsLabel.setText(f"{self.hitPoints}/{self.maxHitPoints}")
        self.progress.setFormat(self.hitPointsLabel.text())

class Player(QWidget):
    def __init__(self, *args, **kwargs,):
        super().__init__(*args, **kwargs)
        # self.maxHitPoints = maxHitPoints
        # self.hitPoints = self.maxHitPoints
        # self.maxMagicPoints = maxMagicPoints
        # self.magicPoints = self.maxMagicPoints
        self.hitPoints = 20

        self.hp = HitPointsDisplay(parent=self)
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # self.textbox.textChanged.connect(self.textbox_text_changed)

        self.layout.addWidget(self.hp, 0, 0)
        # self.layout.addWidget(self.hitPointsLabel, 1, 0)

    def textbox_text_changed(self):
        self.hitPointsLabel.setText(self.textbox.text())
