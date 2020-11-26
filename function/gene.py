from typing import List, Union


class Gene:
    """
    Gene

    26*2개의 유전자형을 가지며 각각은 알파벳 대소문자
    """

    def __init__(self, length: int, genotype: Union[None, List[str]] = None) -> None:
        self.length: int = length
        if genotype:
            self.genotype: List[str] = genotype
        else:
            self.genotype: List[str] = []

    @classmethod
    def crossover(cls, a: 'Gene', b: 'Gene') -> 'Gene':
        return Gene(a.length, a.genotype)
