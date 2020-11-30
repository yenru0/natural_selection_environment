from __future__ import annotations
from typing import Tuple, List, Any, TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from .entity import AbstractEntity


class World:
    """
    자유 월드
    """

    def __init__(self, size: Tuple[int, int]):
        self.size = size
        self.surf: pygame.Surface = pygame.Surface(self.size)
        self.entities: List[AbstractEntity] = list()

    def push_entity(self, entity: AbstractEntity):
        self.entities.append(entity)


class GridWorld:
    """
    그리드 월드
    """

    def __init__(self, gridcellSize: Tuple[int, int], gridCount: Tuple[int, int]):
        self.gridcellSize = gridcellSize
        self.gridCount = gridCount
        self.size = (gridcellSize[0] * gridCount[0], gridcellSize[1] * gridCount[1])
        self.surface: pygame.Surface = pygame.Surface(self.size)
        self.entities: List[AbstractEntity] = list()

        self.gridProperty: List[List[Any]] = [[None] * gridCount[1] for _ in range(gridCount[0])]

    def push_entity(self, entity: AbstractEntity):
        self.entities.append(entity)

    def gridInEntity(self, entity: AbstractEntity):
        """
        엔티티
        :param entity:
        :return: gridIndex
        """
        pass

    def draw_grid(self):
        self.surface.fill((255, 255, 255))
        for i in range(self.gridCount[0]):
            pygame.draw.line(self.surface, (0, 0, 0),
                             (self.gridcellSize[0] * (i + 1), 0),
                             (self.gridcellSize[0] * (i + 1), self.size[1]))
        for j in range(self.gridCount[1]):
            pygame.draw.line(self.surface, (0, 0, 0),
                             (0, self.gridcellSize[1] * (j + 1)),
                             (self.size[0], self.gridcellSize[1] * (j + 1),))

    def fill_cell(self, x, y, color):
        self.surface.fill(color,
                          (self.gridcellSize[0] * x + 1, self.gridcellSize[1] * y + 1,
                           self.gridcellSize[0] - 1, self.gridcellSize[1] - 1)
                          )

    def draw(self):
        """
        상속받는 입장에서 커스텀한 월드를 구현해야됨
        :return:
        """
        pass
