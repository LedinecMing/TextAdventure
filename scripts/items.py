import typing
import dataclasses

from materials import Component


@dataclasses.dataclass()
class Item:
    name: str
    _materials: typing.Dict[Component, float]
    _tags: typing.Dict = dataclasses.field(default_factory=dict)

    def __hash__(self):
        return self.name.__hash__()

    @property
    def weight(self):
        return sum([key.density * value for key, value in self._materials.items()])

    @property
    def tags(self):
        return self._tags

    @property
    def materials(self):
        return self._materials


@dataclasses.dataclass()
class Weapon(Item):
    _damage: float = 1

    @property
    def damage(self):
        return self._damage


@dataclasses.dataclass()
class Armor(Item):
    _defence: float = 1

    @property
    def defence(self):
        return self._defence


