import logging
from pathlib import Path

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QGraphicsScene, QGraphicsView, QVBoxLayout, QPushButton
from PyQt5 import QtCore

logger = logging.getLogger("character_entry_widget")


def load_pixmaps(images_path: str, max_value: int):
    pixmaps = []
    for i in range(0, max_value):
        value_filename = f"0x0{i:X}.png"
        # print(f"{i:2}: {value_filename}")
        file_path = Path(images_path) / value_filename
        new_pixmap = QPixmap(str(file_path))
        pixmaps.append(new_pixmap)
        print(new_pixmap)
    # print("pixmaps: ", pixmaps)
    return pixmaps


class PasswordCharacterEntry(QWidget):
    MAX_VALUE = 0x10  # 16

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.value = 0

        self.alphabet_pixmaps = load_pixmaps("images/alphabet", self.MAX_VALUE)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # self.textbox.textChanged.connect(self.textbox_text_changed)

        self.upButton = QPushButton("+")
        self.downButton = QPushButton("-")

        self.upButton.clicked.connect(self.count_up)
        self.downButton.clicked.connect(self.count_down)
        self.binaryLabel = QLabel()
        self.currentPixmap = self.alphabet_pixmaps[self.value]
        self.scene = QGraphicsScene(0, 0, 70, 80)
        self.view = QGraphicsView(self.scene)
        self.scene.addPixmap(self.currentPixmap)
        self.scene.update()
        self.layout.setSpacing(0)
        self.layout.addWidget(self.upButton)
        self.layout.addWidget(self.view)
        self.layout.addWidget(self.downButton)
        self.layout.addWidget(self.binaryLabel)
        self.show()
        self.update()

        # self.layout.addWidget(self.progress, 1, 0, 1, 2)
        logger.info("%s instance created. value = %s. currentPixmap = %s", self.__class__.__name__, self.value, self.currentPixmap)

    @QtCore.pyqtSlot()
    def count_up(self):
        self.value += 1
        if self.value == 16:
            self.value = 0
        self.scene.clear()
        self.currentPixmap = self.alphabet_pixmaps[self.value]
        self.scene.addPixmap(self.currentPixmap)
        self.scene.update()
        self.binaryString =  f"{self.value:04b}" #bin(self.value).split('b', 1)[1]
        self.binaryLabel.setText(self.binaryString)

    @QtCore.pyqtSlot()
    def count_down(self):
        self.value -= 1
        if self.value == -1:
            self.value = 15
        self.scene.clear()
        self.currentPixmap = self.alphabet_pixmaps[self.value]
        self.scene.addPixmap(self.currentPixmap)
        self.scene.update()
        self.binaryString =  f"{self.value:04b}"
        self.binaryLabel.setText(self.binaryString)