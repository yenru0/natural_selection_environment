from __future__ import annotations
from typing import TYPE_CHECKING, Tuple
import random

from PySide2 import QtWidgets

if TYPE_CHECKING:
    from .gui import MainWindow
from .world import BadukWorld, GridWorld, FloatWorld, TendencyWorld
from .entity import Baduk, RandomMover, Mover
from .gene import Gene


def dispatch(args: str) -> dict:
    ret = dict()
    for i in args.split(";"):
        t = i.split("=")
        if len(t) != 2:
            continue
        else:
            ret[t[0].strip()] = t[1].strip()
    return ret


class GuiInstance:
    default_args = ""
    description = ""

    def __init__(self, gui):
        self.world: GridWorld = None
        self.gui: MainWindow = gui

    def make_world(self, gridcellSize: Tuple[int, int], gridCount: Tuple[int, int]) -> GridWorld:
        pass

    def make_panel(self):
        pass

    def fresh(self):
        pass

    def draw(self):
        pass

    def init_world(self):
        pass

    def make_progress(self):
        pass

    def make_spawn(self):
        pass

    def start_world(self):
        pass

    def stop_world(self):
        pass


class Resistance(GuiInstance):
    default_args = "concentration=2;resistance_rate=0.1"
    description = "과학책에 나온 내성 세균의 번식을 재현한 인스턴스입니다\n" \
                  "-concentration: 항생제의 패턴 높을수록 항생제 그리드가 적어짐\n" \
                  "-resistance_rate: 초기 저항성 개체의 생성 확률\n"
    default_value = {"concentration": 2, "resistance_rate": 0.1}

    def __init__(self, gui):
        super().__init__(gui)
        self.value: dict = {
            "concentration": 2,
            "resistance_rate": 0.1
        }

    def make_world(self, gridcellSize: Tuple[int, int], gridCount: Tuple[int, int]) -> GridWorld:
        self.world = BadukWorld(gridCount=gridCount, gridcellSize=gridcellSize)
        return self.world

    def fresh(self):
        pass

    def draw(self):
        self.world.draw()

    def init_world(self):
        t = dispatch(self.gui.ledit_args.text())
        if "concentration" in t:
            self.value["concentration"] = int(t["concentration"])
        else:
            self.value["concentration"] = self.default_value["concentration"]
        if "resistance_rate" in t:
            self.value["resistance_rate"] = float(t["resistance_rate"])
        else:
            self.value["resistance_rate"] = self.default_value["resistance_rate"]

        for i in range(self.world.gridCount[0]):
            for j in range(self.world.gridCount[1]):
                if (i + j) % self.value["concentration"] == 0:
                    self.world.gridProperty[i][j] = 0
                else:
                    self.world.gridProperty[i][j] = 1

        for i in range(self.gui.spbox_initspawn.value()):
            if random.random() < self.value["resistance_rate"]:
                self.world.push_entity(Baduk(self.world, gene=Gene(1, "BADUK", genotype=[1])))
            else:
                self.world.push_entity(Baduk(self.world, gene=Gene(1, "BADUK", genotype=[0])))
        self.gui.textli.insertPlainText(f"초기화 완료: {self.value}\n")
        self.gui.textli.insertPlainText(self.description)

        if len(self.world.entities):
            self.gui.textli.insertPlainText(("===" * 4) + f"{self.world.gen}\n"
                                            + f"내성 비율: {len(self.world.find_entities_with_condition(lambda v: v.gene.genotype[0] == 1)) / len(self.world.entities)}\n")
        else:
            self.gui.textli.insertPlainText(("===" * 4) + f"{self.world.gen}\n"
                                            + f"내성 비율: None\n")

    def make_progress(self):
        self.world.make_progress()
        self.world.make_post_progress()
        self.gui.view_progression.setText(f"{self.world.gen}")
        self.gui.view_entities.setText(
            f"{len(self.world.entities)}: 내성{len(self.world.find_entities_with_condition(lambda v: v.gene.genotype[0] == 1))}/비내성{len(self.world.find_entities_with_condition(lambda v: v.gene.genotype[0] == 0))}")
        if len(self.world.entities):
            self.gui.textli.insertPlainText(("===" * 4) + f"{self.world.gen}\n"
                                            + f"내성 비율: {len(self.world.find_entities_with_condition(lambda v: v.gene.genotype[0] == 1)) / len(self.world.entities)}\n")
        else:
            self.gui.textli.insertPlainText(("===" * 4) + f"{self.world.gen}\n"
                                            + f"내성 비율: None\n")
        self.gui.textli.verticalScrollBar().setValue(self.gui.textli.verticalScrollBar().maximum())

    def make_spawn(self):
        [self.world.push_entity(e) for e in [Baduk(self.world) for _ in range(self.gui.spbox_spawn_count.value())]]

    def start_world(self):
        self.make_progress()
        self.gui.fresh()

    def stop_world(self):
        pass


class RandomWalk(GuiInstance):
    description = "랜덤 워크 인스턴스입니다\n"

    def make_world(self, gridcellSize: Tuple[int, int], gridCount: Tuple[int, int]) -> GridWorld:
        self.world = FloatWorld(gridCount=gridCount, gridcellSize=gridcellSize)
        return self.world

    def fresh(self):
        self.world.update()
        self.gui.frame_number += 1
        self.gui.view_progression.setText(str(self.gui.frame_number))

    def draw(self):
        self.world.draw()

    def init_world(self):
        for i in range(self.gui.spbox_initspawn.value()):
            self.world.push_entity(RandomMover(self.world))
        self.gui.textli.insertPlainText("초기화 완료\n")
        self.gui.textli.insertPlainText(self.description)

    def make_progress(self):
        pass

    def make_spawn(self):
        [self.world.push_entity(e) for e in [RandomWalk(self.world) for _ in range(self.gui.spbox_spawn_count.value())]]

    def start_world(self):
        self.gui.fresh_timer.start()

    def stop_world(self):
        self.gui.fresh_timer.stop()


class Tendency(GuiInstance):
    default_args = "destination=(0, 0);spawnpoint=middle"
    description = "어떤 목표를 향해 달려가는 개체들"
    default_value = {"destination": "middle", "spawnpoint": "middle"}

    def __init__(self, gui):
        super().__init__(gui)
        self.value = {
            "destination": (0, 0),
            "spawnpoint": (100, 100)
        }

    def make_world(self, gridcellSize: Tuple[int, int], gridCount: Tuple[int, int]) -> GridWorld:
        self.world = TendencyWorld(gridCount=gridCount, gridcellSize=gridcellSize)
        return self.world

    def fresh(self):
        self.world.update()
        self.gui.view_progression.setText(f"{self.world.gen}/{self.gui.frame_number}")
        self.gui.frame_number += 1
        if self.gui.frame_number % 200 == 0:
            self.make_progress()

    def draw(self):
        self.world.draw()

    def start_world(self):
        self.gui.fresh_timer.start()

    def stop_world(self):
        self.gui.fresh_timer.stop()

    def init_world(self):
        def point_check(self, s: str):
            if s not in ["middle"]:
                return None
            if s == "middle":
                return self.world.gridcellSize[0] / 2, self.world.gridcellSize[1] / 2

        t = dispatch(self.gui.ledit_args.text())
        if "destination" in t:
            v = t["destination"]
            c = point_check(self, v)

            if c is None:
                v = eval(v)
                if isinstance(v, tuple):
                    if len(v) == 2:
                        self.value["destination"] = v
                    else:
                        raise Exception("not len 2")
                else:
                    raise Exception("invalid type")
            else:
                self.value["destination"] = c
        else:
            self.value["destination"] = point_check(self, self.default_value["destination"])

        if "spawnpoint" in t:
            v = t["spawnpoint"]
            c = point_check(self, v)
            if c is None:
                v = eval(v)
                if isinstance(v, tuple):
                    if len(v) == 2:
                        self.value["spawnpoint"] = v
                    else:
                        raise Exception("not len 2")
                else:
                    raise Exception("invalid type")
            else:
                self.value["spawnpoint"] = c
        else:
            self.value["spawnpoint"] = point_check(self, self.default_value["spawnpoint"])

        self.world.destination = self.value["destination"]
        self.world.spawnpoint = self.value["spawnpoint"]
        self.world.gene_length = 200

        # 엔티티 소환
        [self.world.push_entity(e) for e in [Mover(self.world) for _ in range(self.gui.spbox_initspawn.value())]]

        self.gui.textli.insertPlainText(f"초기화 완료: {self.value}\n")
        self.gui.textli.insertPlainText(self.description)

    def make_progress(self):
        self.world.make_progress()
        self.world.make_post_progress()
        self.gui.textli.insertPlainText(f"==={self.world.gen}\n")
        self.gui.textli.insertPlainText(f"best: {max(self.world.fitness_pool)}, worst: {min(self.world.fitness_pool)}\n")
        self.gui.textli.verticalScrollBar().setValue(self.gui.textli.verticalScrollBar().maximum())

    def make_spawn(self):
        pass
