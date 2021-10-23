import dataclasses
import typing


@dataclasses.dataclass(unsafe_hash=True)
class Component:
    _density: float

    @property
    def density(self):
        return self._density


@dataclasses.dataclass(unsafe_hash=True)
class Material(Component):
    _name: str


class Alloy(Component):
    def __init__(self, name: str, *materials: typing.Tuple[Material, float]) -> None:
        self.name: str = name
        if sum([percent[1] for percent in materials]) != 1:
            raise ValueError("Alloy's materials percents are not 100 in sum")
        self._materials: typing.Dict[Material, float] = {material_info[0]: material_info[1] for material_info in materials}

    @property
    def density(self) -> float:
        return sum([material.density * percent for material, percent in self._materials.items()])

