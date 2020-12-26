import random

import numpy as np

from .body import AbstractBody, BadukBody, CircleBody
from .gene import Gene
from .etc import PerlinNoiseFactory


class AbstractEntity:
    """
    Entity는 단지 개체의 정보를 모아 놓습니다.
    """

    def __init__(self, world, identifier):
        self.world = world
        self.body: AbstractBody = AbstractBody(self)
        self.identifier = identifier
        self.gene: Gene = Gene(1, identifier)
        self.age: int = 0

    def update(self):
        pass

    @classmethod
    def mate(cls, a: 'AbstractEntity', b: 'AbstractEntity') -> 'AbstractEntity':
        pass

    def draw(self):
        self.body.draw()

    def copy(self):
        pass

    def aging(self):
        self.age += 1


class RandomMover(AbstractEntity):
    def __init__(self, world):
        super().__init__(world, "RW")
        self.body = CircleBody(self)
        self.body.position = [self.world.size[0] / 2, self.world.size[1] / 2]

    def update(self):
        self.body.position = [self.body.position[0] + random.randint(-1, 1),
                              self.body.position[1] + random.randint(-1, 1)]

    def copy(self) -> 'RandomMover':
        return RandomMover(self.world)


class Baduk(AbstractEntity):
    def __init__(self, world, gene=None):
        super().__init__(world, "BADUK")
        self.body = BadukBody(self)
        self.body.position = [random.randint(0, self.world.size[0]), random.randint(0, self.world.size[1])]
        if gene is not None:
            if gene.identifier == self.identifier:
                self.gene = gene.clone()
            else:
                raise Exception("wrong identi")
        else:
            self.gene = Gene(1, identifier=self.identifier, genotype=[0])

    def copy(self) -> 'Baduk':
        return Baduk(self.world, gene=self.gene.clone())
