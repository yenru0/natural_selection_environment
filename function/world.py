from __future__ import annotations

import random
from typing import Tuple, List, Any, Callable, TYPE_CHECKING

import numpy as np
import pygame

if TYPE_CHECKING:
    from .entity import AbstractEntity
from .gene import GeneUtility


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
        self.gen = 0

    def push_entity(self, entity: AbstractEntity):
        """
        엔티티를 추가한다.
        :param entity: 추가할 엔티티
        """
        self.entities.append(entity)

    def eliminate_entity(self, entity: AbstractEntity):
        """
        월드에 속한 엔티티를 지운다.
        :param entity: 지울 엔티티
        """
        self.entities.remove(entity)

    def get_cell_in_entity(self, entity: AbstractEntity) -> Tuple[int, int]:
        """
        엔티티가 속한 그리드 셀의 위치를 반환
        :param entity: 찾을 엔티티
        :return: 셀 위치좌표, (X 인덱스, Y 인덱스)
        """
        return (entity.body.position[0] // self.gridcellSize[0]), (entity.body.position[1] // self.gridcellSize[1])

    def find_entities_with_condition(self, condition: Callable) -> Tuple:
        return tuple(filter(condition, self.entities))

    def draw_grid(self, color=(0, 0, 0), backcolor=(255, 255, 255)):
        """
        배경을 단색으로 채우고 그리드를 그림
        :param color: 그리드 선 색
        :param backcolor: 배경 색
        """
        self.surface.fill(backcolor)
        for i in range(self.gridCount[0]):
            pygame.draw.line(self.surface, color,
                             (self.gridcellSize[0] * (i + 1), 0),
                             (self.gridcellSize[0] * (i + 1), self.size[1]))
        for j in range(self.gridCount[1]):
            pygame.draw.line(self.surface, color,
                             (0, self.gridcellSize[1] * (j + 1)),
                             (self.size[0], self.gridcellSize[1] * (j + 1),))

    def fill_cell(self, x: int, y: int, color):
        """
        특정 인덱스의 그리드 셀을 채움
        :param x: 그리드 셀 X 인덱스
        :param y: 그리드 셀 Y 인덱스
        :param color: 그리드 셀 색
        """
        self.surface.fill(color,
                          (self.gridcellSize[0] * x + 1, self.gridcellSize[1] * y + 1,
                           self.gridcellSize[0] - 1, self.gridcellSize[1] - 1)
                          )

    # after this you implemented

    def update(self):
        """
        프레임이 한번 움직일 동안 진행될 행동을 정의
        예를 들어
        - 엔티티의 업데이트
        - 엔티티의 업데이트로 부터 변화한 월드의 업데이트
        """
        pass

    def draw(self):
        """
        프레임 한번에 그릴 것들을 정의
        예를 들어
        ```
        def draw(self):
            self.draw_grid()
            for e in self.entities:
                e.draw()
        ```
        이런식으로 월드 뿐만 아니라 그 월드에 속한 엔티티또한 그려줌
        """
        pass

    def make_progress(self):
        """
        세계의 전체적인 진보를 일으킴
        예를 들면 교배를 일으키거나 등등
        무조건 gen(세대) 수치는 1 증가해야됨
        """
        self.gen += 1

    def make_pre_progress(self):
        """
        진보를 일으키기 전 전처리 정의
        """
        pass

    def make_post_progress(self):
        """
        진보를 일으키고 후처리 정의
        """
        pass

    def fitness(self, e) -> float:
        """
        엔티티의 적합도를 반환합니다.
        :param e: 적합도를 구할 엔티티
        :return: fitness
        """
        pass


class FreeWorld(GridWorld):
    def __init__(self, gridcellSize: Tuple[int, int], gridCount: Tuple[int, int]):
        super().__init__((gridcellSize[0] * gridCount[0], gridcellSize[1] * gridCount[1]), (1, 1))


class FloatWorld(FreeWorld):
    def draw(self):
        self.fill_cell(0, 0, (255, 255, 255))
        for e in self.entities:
            e.draw()

    def update(self):
        for e in self.entities:
            e.update()


class BadukWorld(GridWorld):
    def __init__(self, gridcellSize: Tuple[int, int], gridCount: Tuple[int, int]):
        super().__init__(gridcellSize, gridCount)

    def draw(self):
        self.draw_grid()
        for i, row in enumerate(self.gridProperty):
            for j, cell in enumerate(row):
                if cell == 1:
                    self.fill_cell(i, j, (80, 80, 80))
        # entities
        for e in self.entities:
            e.draw()

    def make_progress(self):
        for e in self.entities[:]:
            t = e.gene.genotype[0]
            ix, iy = self.get_cell_in_entity(e)
            if self.gridProperty[ix][iy] == 1:
                if t == 0:
                    self.eliminate_entity(e)
        for e in self.entities[:]:
            self.push_entity(e.copy())
        self.gen += 1

    def make_post_progress(self):
        for e in self.entities:
            e.body.position = [random.randrange(0, self.size[0]), random.randrange(0, self.size[1])]


class TendencyWorld(FreeWorld):
    def __init__(self, gridcellSize: Tuple[int, int], gridCount: Tuple[int, int]):
        super().__init__(gridcellSize, gridCount)
        self.destination: Tuple[float, float] = (0, 0)
        self.spawnpoint: Tuple[float, float] = (0, 0)
        self.gene_length: int = 200
        self.frame: int = 0
        self.fitness_pool: list = []

    def draw(self):
        self.fill_cell(0, 0, (255, 255, 255))
        pygame.draw.circle(self.surface, (30, 30, 170), (int(self.destination[0]), int(self.destination[1])), 10)
        for e in self.entities:
            e.draw()

    def update(self):
        for e in self.entities:
            e.update()
        self.frame += 1

    def make_progress(self):
        gene_pool = []
        self.fitness_pool = []

        count = len(self.entities)
        for e in self.entities[:]:
            g, f = e.gene, self.fitness(e)
            if f == 0:
                f = 0.000000000000000000000000000001
            gene_pool.append(g)
            self.fitness_pool.append(f)
        sum_of_fitness = sum(self.fitness_pool)

        def choice() -> int:
            p = np.random.uniform(0, sum_of_fitness)
            t = 0
            for i in range(0, count):
                t += self.fitness_pool[i]
                if p < t:
                    return i

        for i in range(count):
            _a = gene_pool[choice()]
            _b = gene_pool[choice()]
            _n = GeneUtility.mutate(GeneUtility.crossover_half(_a, _b),
                                    lambda: (random.uniform(-3, 3), random.uniform(-3, 3))
                                    )
            self.entities[i].gene = _n

        self.gen += 1

    def make_post_progress(self):
        self.frame = 0
        for e in self.entities:
            e.body.position = list(self.spawnpoint)

    def fitness(self, e: AbstractEntity) -> float:
        return 1 / np.sqrt(
            ((self.destination[0] - e.body.position[0]) ** 2 + (self.destination[1] - e.body.position[1]) ** 2))
