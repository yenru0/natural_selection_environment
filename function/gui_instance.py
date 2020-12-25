from __future__ import annotations
from typing import TYPE_CHECKING, Tuple
import random

if TYPE_CHECKING:
    from .gui import MainWindow
from .world import BadukWorld, GridWorld
from .entity import Baduk
from .gene import Gene


class Resistance:
    def __init__(self, gui):
        self.world: GridWorld
        self.gui: MainWindow = gui

    def make_world(self, gridcellSize: Tuple[int, int], gridCount: Tuple[int, int]) -> GridWorld:
        self.world = BadukWorld(gridCount=gridCount, gridcellSize=gridcellSize)
        return self.world

    def fresh(self):
        pass

    def draw(self):
        self.world.draw()

    def init_world(self):
        for i in range(self.world.gridCount[0]):
            for j in range(self.world.gridCount[1]):
                if (i + j) % 2 == 0:
                    self.world.gridProperty[i][j] = 0
                else:
                    self.world.gridProperty[i][j] = 1

        for i in range(self.gui.spbox_initspawn.value()):
            if random.random() < 0.1:
                self.world.push_entity(Baduk(self.world, gene=Gene(1, "BADUK", genotype=[1])))
            else:
                self.world.push_entity(Baduk(self.world, gene=Gene(1, "BADUK", genotype=[0])))

    def make_progress(self):
        self.world.make_progress()
        self.world.make_post_progress()
        self.gui.view_progression.setText(f"{self.world.gen}")
        self.gui.view_entities.setText(
            f"{len(self.world.entities)}: 내성{len(self.world.find_entities_with_condition(lambda v: v.gene.genotype[0] == 1))}/비내성{len(self.world.find_entities_with_condition(lambda v: v.gene.genotype[0] == 0))}")

    def make_spawn(self):
        [self.world.push_entity(e) for e in [Baduk(self.world) for _ in range(self.gui.spbox_spawn_count.value())]]

    def start_world(self):
        self.make_progress()
        self.gui.fresh()

    def stop_world(self):
        pass


class RandomWalk:
    def __init__(self, gui):
        self.world: GridWorld
        self.gui: MainWindow = gui

    def make_world(self, gridcellSize: Tuple[int, int], gridCount: Tuple[int, int]) -> GridWorld:
        self.world = BadukWorld(gridCount=gridCount, gridcellSize=gridcellSize)
        return self.world

    def fresh(self):
        pass

    def draw(self):
        self.world.draw_grid((255, 0, 0), (100, 100, 100))

    def init_world(self):
        for i in range(self.world.gridCount[0]):
            for j in range(self.world.gridCount[1]):
                if (i + j) % 2 == 0:
                    self.world.gridProperty[i][j] = 1
                else:
                    self.world.gridProperty[i][j] = 0

    def make_progress(self):
        pass

    def make_spawn(self):
        [self.world.push_entity(e) for e in [Baduk(self.world) for _ in range(self.gui.spbox_spawn_count.value())]]

    def start_world(self):
        pass

    def stop_world(self):
        pass
