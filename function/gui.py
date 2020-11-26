from __future__ import annotations
from typing import TYPE_CHECKING
import random

from PySide2 import QtGui, QtWidgets, QtCore
import pygame

from .ui.MainWindow import Ui_MainWindow


class PygameWidget(QtWidgets.QWidget):
    def __init__(self, surface: pygame.Surface, parent=None):
        super().__init__(parent)

        self.surface = surface
        self.data: bytes
        self.image: QtGui.QImage
        self.fresh()

    def paintEvent(self, event: QtGui.QPaintEvent):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.drawImage(0, 0, self.image)
        qp.end()

    def fresh(self):
        w = self.surface.get_width()
        h = self.surface.get_height()
        self.setMinimumSize(w, h)
        self.data = self.surface.get_buffer().raw
        self.image: QtGui.QImage = QtGui.QImage(self.data, w, h, QtGui.QImage.Format_RGB32)
        self.update()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, surface: pygame.Surface, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.surface = surface

        self.pygame_w = PygameWidget(surface, self.pygame_container)
        self.pygame_container.setMinimumSize(surface.get_width(), surface.get_height())

        self.setWindowTitle("Main")

        self.fresh_timer = QtCore.QTimer()
        self.fresh_timer.setInterval(1000 / 60)
        self.fresh_timer.timeout.connect(self.fresh)
        self.fresh_timer.start()

        self.test_poss = [[random.randint(100, 400), random.randint(100, 400)] for _ in range(10)]

        self.btn.clicked.connect(self.btn_c)


    def fresh(self):
        self.draw()
        self.pygame_w.fresh()

    def draw(self):
        self.surface.fill((64, 128, 192, 224))

        for pos in self.test_poss:
            pos[0] += random.randint(-2, 2)
            pos[1] += random.randint(-2, 2)
            pygame.draw.circle(self.surface, (255, 255, 255, 255), pos, 10)
