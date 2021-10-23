import typing
import dataclasses
from items import Armor, Weapon, Item


@dataclasses.dataclass()
class Inventory:
    _armor: Armor | None
    _weapon: Weapon | None
    _items: typing.Dict[Item, float]

    def __setitem__(self, item, value) -> None:
        if value not in self._items:
            self._items[item] = 0
        self._items[item] += 1

    def __getitem__(self, item) -> float:
        if item not in self._items:
            self._items[item] = 0
        return self._items[item]

    @property
    def weight(self) -> float:
        weight: float = 0
        if self._armor is not None:
            weight += self._armor.weight
        if self._weapon is not None:
            weight += self._weapon.weight
        return weight + sum([item.weight for item in self._items.keys()])

    @property
    def armor(self) -> Armor:
        return self._armor

    @property
    def weapon(self) -> Weapon:
        return self._weapon

    @property
    def items(self) -> typing.Dict[Item, float]:
        return self._items

    def update_item(self, old_item, new_item) -> None:
        self._items[old_item] -= 1
        if not (new_item in self._items.keys()):
            self._items[new_item] = 0
        self._items[new_item] += 1


@dataclasses.dataclass()
class Statistics:
    _damage: int
    _health: typing.MutableSequence
    _strength: int
    _stamina: typing.MutableSequence

    @property
    def damage(self) -> int:
        return self._damage

    @property
    def health(self) -> typing.MutableSequence:
        return self._health

    @property
    def strength(self) -> int:
        return self._strength

    @property
    def stamina(self) -> typing.MutableSequence:
        return self._stamina
