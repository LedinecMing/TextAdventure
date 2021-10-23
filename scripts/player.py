import typing

import colorama

from inventory import Inventory, Statistics
from items import Armor, Weapon, Item
from materials import Material, Alloy, Component
from to_ascii import show_gif, print_image, clear_term, get_terminal_size, generate_image
from math import ceil
import dataclasses
import time
import random


@dataclasses.dataclass()
class Player:
    name: str
    inventory: Inventory
    stats: Statistics

    def attack(self, enemy) -> int:
        if random.randint(0, 100) > 90:
            return 0
        if self.inventory.weight > self.stats.strength and random.randint(0, 100) > 60:
            return 0
        return self.stats.damage + self.inventory.weapon.damage - enemy.inventory.armor.defence


gel: Material = Material(200, "Гель")
wood: Material = Material(700, "Дуб")
cloth: Material = Material(1500, "Ткань"
                           )
slime: Player = Player("Slime",
                       Inventory(
                           Armor("Гелевая оболочка",
                                 {gel: 0.2},
                                 {}, 2),
                           Weapon("Гель",
                                  {gel: 0.3},
                                  {"no_drop": True}, 3),
                           {Item("Шарик геля", {gel: 0.5}): 2}
                       ),
                       Statistics(0, [40, 40], 200, [10, 10])
                       )
player: Player = Player("you",
                        Inventory(
                            Armor("Одежда",
                                  {cloth: 0.01},
                                  {}, 1),
                            Weapon("Палка",
                                   {wood: 0.005},
                                   {}, 5),
                            {}
                        ),
                        Statistics(3, [100, 100], 100, [50, 50])
                        )


def print_centered(text: str) -> None:
    term_size: typing.Tuple[int, int] = get_terminal_size()
    print(" " * ((term_size[0] - len(text)) // 2) + text + " " * ((term_size[0] - len(text)) // 2))


while slime.stats.health[0] > 0 < player.stats.health[0]:
    damage: int = slime.attack(player)
    player.stats.health[0] -= damage
    damage: int = player.attack(slime)
    slime.stats.health[0] -= damage
    health_bar = colorama.Fore.RED + "█" * ceil(slime.stats.health[0] / slime.stats.health[1] * 10)
    print_centered("Slime")
    print_centered(health_bar)
    print_image(f"img/{slime.name}.png", 40, 40, center=True)
    time.sleep(1.5)
    clear_term()
print_centered("Slime проиграл")
print_centered("Вы получили: " + str(slime.inventory.items))
for k, v in slime.inventory.items.items():
    player.inventory[k] += 1
print_centered("Ваши вещи: " + str(player.inventory.items))
i = generate_image("img/leather_chestplate.png", 20, 15, center=True)
j = generate_image("img/Stick.png", 4, 15)
for x in range(0, 15):
    to_write: str = i.__next__()
    print(" " * ceil((get_terminal_size()[0] - 18)/2) + to_write, j.__next__())
print_image("img/jeans.png", 20, 15)
