import sys

import pygame
from PySide2.QtWidgets import QApplication

from function.body import AbstractBody
from function.entity import AbstractEntity
from function.gene import Gene
from function.species import Species
from function.gui import MainWindow

if __name__ == '__main__':
    pygame.init()
    surf = pygame.Surface((640,480))
    app = QApplication(sys.argv)
    w = MainWindow(surf)
    #w.setFixedSize(650, 490)
    w.show()
    app.exec_()