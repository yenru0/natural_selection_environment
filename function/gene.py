import random
from typing import List, Union, Callable, Any

import numpy as np

class Gene:
    """
    Gene

    genotype은 유전자 리스트
    """

    def __init__(self, length: int, identifier: str,
                 mutation_rate: float = .05, genotype: Union[None, List[Any]] = None):
        self.length: int = length
        self.identifier: str = identifier
        self.mutation_rate: float = mutation_rate
        if genotype:
            if len(genotype) != length:
                raise Exception("wrong genotype")
            self.genotype: List[Any] = genotype
        else:
            self.genotype: List[Any] = [None] * length

    def clone(self):
        return Gene(self.length, self.identifier, mutation_rate=self.mutation_rate, genotype=self.genotype)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"<GENE:{self.identifier}({self.length}):{self.genotype}({self.mutation_rate})>"


class GeneUtility:
    """
    Gene과 관련된 여러가지 연산을 합니다.
    """

    @staticmethod
    def crossover_half(a: Gene, b: Gene) -> Gene:
        return Gene(a.length, a.identifier,
                    mutation_rate=a.mutation_rate,
                    genotype=a.genotype[:int(a.length / 2)] + b.genotype[int(a.length / 2):])

    @staticmethod
    def mutate(a: Gene, make: Callable[[], Any]) -> Gene:
        for i in range(a.length):
            if random.random() < a.mutation_rate:
                a.genotype[i] = make()
        return a


# test
if __name__ == '__main__':
    g1 = Gene(1, "T", genotype=[0, ], mutation_rate=0.5)
    g2 = Gene(1, "T", genotype=[0, ], mutation_rate=0.5)

    print(g1.clone())
