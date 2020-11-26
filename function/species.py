from .entity import AbstractEntity

from typing import List


class Species:
    def __init__(self, name: str):
        self.name: str = name
        self.entities: List[AbstractEntity] = []

    def update(self):
        for e in self.entities:
            e.update()
