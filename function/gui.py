from __future__ import annotations
from typing import TYPE_CHECKING
import random

from PySide2 import QtGui, QtWidgets, QtCore
import pygame
import numpy as np

from .ui.MainWindow import Ui_MainWindow
from .etc import noise_xerius2, PerlinNoiseFactory
if TYPE_CHECKING:
    from .world import GridWorld


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
    def __init__(self, world: GridWorld, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.world = world

        self.surface: pygame.Surface = world.surface

        self.pygame_w = PygameWidget(self.surface, self.pygame_container)
        self.pygame_container.setMinimumSize(self.surface.get_width(), self.surface.get_height())

        self.setWindowTitle("Main")

        self.fresh_timer = QtCore.QTimer()
        self.frame_number = 0
        self.fresh_timer.setInterval(1000 / 1)
        self.fresh_timer.timeout.connect(self.fresh)
        self.fresh_timer.start()

        for i in range(self.world.gridCount[0]):
            for j in range(self.world.gridCount[1]):
                if (i + j) % 2 == 0:
                    self.world.gridProperty[i][j] = True
                else:
                    self.world.gridProperty[i][j] = False

    def fresh(self):
        self.draw()
        self.pygame_w.fresh()

    def draw(self):
        self.world.draw_grid()
        for i, row in enumerate(self.world.gridProperty):
            for j, cell in enumerate(row):
                if cell:
                    self.world.fill_cell(i, j, (100, 100, 100))
        # self.surface = pygame.surfarray.make_surface(self.t)
        # self.pygame_w.surface = self.surface
        # self.surface.fill((pn, pn, pn), (x, y, 1, 1))
