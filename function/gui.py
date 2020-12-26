from __future__ import annotations
from typing import TYPE_CHECKING
import random

from PySide2 import QtGui, QtWidgets, QtCore
import pygame
import numpy as np

from .ui.MainWindow import Ui_MainWindow
from .etc import noise_xerius2, PerlinNoiseFactory
from .entity import Baduk
from .world import GridWorld
from .gui_instance import Resistance, RandomWalk


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

    def setSurface(self, surface: pygame.Surface):
        self.surface = surface


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Main")

        self.comboList = [Resistance(self), RandomWalk(self)]
        self.comboBox.addItems(["resistance", "random_walk"])
        self.comboBox.currentIndexChanged.connect(self.combo_change)
        # self.comboBox.currentTextChanged.connect(self.combo_change)
        self.comboNow = self.comboList[0]
        self.ledit_args.setText(self.comboNow.default_args)

        # for dynamic world to use update cycle
        self.fresh_timer = QtCore.QTimer()
        self.fps = 60
        self.frame_number = 0
        self.fresh_timer.setInterval(int(1000 / self.fps))
        self.fresh_timer.timeout.connect(self.fresh)

        self.btn_world_start.clicked.connect(self.start_world)
        self.btn_world_stop.clicked.connect(self.stop_world)

        self.btn_spawn.clicked.connect(self.make_spawn)

        self.btn_confirm.clicked.connect(self.init_world)
        self.world: GridWorld = GridWorld((1, 1), (1, 1))

        self.surface: pygame.Surface = self.world.surface

        self.pygame_w = PygameWidget(self.surface, self.pygame_container)

        self.init_world()

    def fresh(self):
        self.comboNow.fresh()
        self.draw()

    def draw(self):
        self.comboNow.draw()
        self.pygame_w.fresh()

    def init_world(self):
        self.fresh_timer.stop()
        self.frame_number = 0
        self.textli.clear()

        self.comboNow.make_panel()
        self.world = self.comboNow.make_world((self.spbox_wg_csX.value(), self.spbox_wg_csY.value()),
                                              (self.spbox_wg_gcX.value(), self.spbox_wg_gcY.value()))

        self.comboNow.init_world()
        self.view_progression.setText(str(self.frame_number))
        self.view_entities.setText(str(len(self.world.entities)))

        self.surface = self.world.surface
        self.pygame_w.setSurface(self.surface)
        self.pygame_container.setMinimumSize(self.surface.get_width(), self.surface.get_height())

        self.draw()

    def make_spawn(self):
        self.comboNow.make_spawn()

    def combo_change(self, i):
        self.comboNow = self.comboList[i]
        self.ledit_args.setText(self.comboNow.default_args)

        self.init_world()

    def start_world(self):
        self.comboNow.start_world()

    def stop_world(self):
        self.comboNow.stop_world()

    def delete_panel(self):
        for i in range(self.scrollAreaWidgetContents.layout().count()):
            self.scrollAreaWidgetContents.layout().itemAt(i).widget().setParent(None)
