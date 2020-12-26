from __future__ import annotations
from typing import TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from .entity import AbstractEntity


class AbstractBody:
    """
    이는 단지 Entity의 물리적 형체를 갖도록 하는 속성 e.g. position, shape 등을 가지며
     월드에 구현토록 하는 draw 메소드를 가집니다.
    """

    def __init__(self, entity: 'AbstractEntity'):
        self.entity: 'AbstractEntity' = entity
        self.position: [float, float] = [0, 0]

    def draw(self):
        pass


class CircleBody(AbstractBody):
    def draw(self):
        pygame.draw.circle(self.entity.world.surface, (255, 0, 0), (int(self.position[0]), int(self.position[1])), 5)


class BadukBody(AbstractBody):
    def draw(self):
        if self.entity.gene.genotype[0] == 0:
            pygame.draw.circle(self.entity.world.surface, (0, 0, 255), (int(self.position[0]), int(self.position[1])),
                               5)
        else:
            pygame.draw.circle(self.entity.world.surface, (255, 0, 0), (int(self.position[0]), int(self.position[1])),
                               5)
