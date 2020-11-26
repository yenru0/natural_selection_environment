from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .entity import AbstractEntity


class AbstractBody:
    def __init__(self, entity: 'AbstractEntity'):
        self.entity: 'AbstractEntity' = entity
