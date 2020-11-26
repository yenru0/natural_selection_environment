from .body import AbstractBody
from .gene import Gene


class AbstractEntity:
    def __init__(self):
        self.body: AbstractBody = AbstractBody(self)
        self.gene: Gene = Gene()

    def update(self):
        pass

    @classmethod
    def crossover(cls, a: 'AbstractEntity', b:'AbstractEntity') -> 'AbstractEntity':
        pass
