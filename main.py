import sys

import pygame
from PySide2.QtWidgets import QApplication

from function.body import AbstractBody
from function.entity import AbstractEntity
from function.gene import Gene
from function.species import Species
from function.gui import MainWindow
from function.world import World, GridWorld

if __name__ == '__main__':
    pygame.init()
    gw = GridWorld(gridcellSize = (32, 32), gridCount=(20, 15))
    app = QApplication(sys.argv)
    win = MainWindow(gw)
    win.show()
    app.exec_()
