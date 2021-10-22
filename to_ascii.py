import typing
import colorama
from PIL import Image

img = Image.open('example.gif')

table: typing.List = [' ', '.', ':', "'", ',', '-', ';', '_', '"', '+', '°', '•', '^', '=', '|', '(', '[', '{', "∆",
                      '©', '®', '&', "$", "@", '%', '#', '¶']

colors = {"GREEN": [colorama.Style.DIM + colorama.Fore.GREEN, colorama.Fore.GREEN,
                    colorama.Style.BRIGHT + colorama.Fore.GREEN, colorama.Style.DIM + colorama.Fore.LIGHTGREEN_EX,
                    colorama.Fore.LIGHTGREEN_EX, colorama.Style.BRIGHT + colorama.Fore.LIGHTGREEN_EX],
          "RED": [colorama.Style.DIM + colorama.Fore.RED, colorama.Fore.RED, colorama.Style.BRIGHT + colorama.Fore.RED,
                  colorama.Style.DIM + colorama.Fore.LIGHTRED_EX, colorama.Fore.LIGHTRED_EX,
                  colorama.Style.BRIGHT + colorama.Fore.LIGHTRED_EX],
          "YELLOW": [colorama.Style.DIM + colorama.Fore.YELLOW, colorama.Fore.YELLOW,
                     colorama.Style.BRIGHT + colorama.Fore.YELLOW, colorama.Style.DIM + colorama.Fore.LIGHTYELLOW_EX,
                     colorama.Fore.LIGHTYELLOW_EX, colorama.Style.BRIGHT + colorama.Fore.LIGHTYELLOW_EX],
          "MAGENTA": [colorama.Style.DIM + colorama.Fore.MAGENTA, colorama.Fore.MAGENTA,
                      colorama.Style.BRIGHT + colorama.Fore.MAGENTA, colorama.Style.DIM + colorama.Fore.LIGHTMAGENTA_EX,
                      colorama.Fore.LIGHTMAGENTA_EX, colorama.Style.BRIGHT + colorama.Fore.LIGHTMAGENTA_EX],
          "CYAN": [colorama.Style.DIM + colorama.Fore.CYAN, colorama.Fore.CYAN,
                   colorama.Style.BRIGHT + colorama.Fore.CYAN, colorama.Style.DIM + colorama.Fore.LIGHTCYAN_EX,
                   colorama.Fore.LIGHTCYAN_EX, colorama.Style.BRIGHT + colorama.Fore.LIGHTCYAN_EX],
          "WHITE": [colorama.Style.DIM + colorama.Fore.WHITE, colorama.Fore.WHITE,
                    colorama.Style.BRIGHT + colorama.Fore.WHITE, colorama.Style.DIM + colorama.Fore.LIGHTWHITE_EX,
                    colorama.Fore.LIGHTWHITE_EX, colorama.Style.BRIGHT + colorama.Fore.LIGHTWHITE_EX],
          "BLACK": [colorama.Style.DIM + colorama.Fore.BLACK, colorama.Fore.BLACK,
                    colorama.Style.BRIGHT + colorama.Fore.BLACK, colorama.Style.DIM + colorama.Fore.LIGHTBLACK_EX,
                    colorama.Fore.LIGHTBLACK_EX, colorama.Style.BRIGHT + colorama.Fore.LIGHTBLACK_EX]}


def color_it(color: tuple) -> str:
    if all([col > 150 for col in color]):
        return colors["WHITE"][round((len(colors["WHITE"]) - 1) / 255 * (color[1] + color[2]) / 2)]
    if all([col < 60 for col in color]):
        return colors["BLACK"][round((len(colors["BLACK"]) - 1) / 255 * (color[1] + color[2]) / 2)]
    if color[1] + color[2] > color[0] * 2:
        return colors["CYAN"][round((len(colors["CYAN"]) - 1) / 255 * (color[1] + color[2]) / 2)]
    if color[0] + color[2] > color[1] * 2:
        return colors["MAGENTA"][round((len(colors["MAGENTA"]) - 1) / 255 * (color[2] + color[1]) / 2)]
    if sum(color[0:2]) > color[2] * 2:
        return colors["YELLOW"][round((len(colors["YELLOW"]) - 1) / 255 * (color[1] + color[0]) / 2)]
    if max(color) == color[1]:
        return colors["GREEN"][round((len(colors["GREEN"]) - 1) / 255 * color[1])]
    if max(color) == color[0]:
        return colors["RED"][round((len(colors["RED"]) - 1) / 255 * color[0])]
    return ""


def convert(depth: int) -> str:
    return table[round((len(table) - 1) / 255 * depth)]


def print_image(path: str) -> None:
    image: Image.Image = Image.open(path)
    image = image.convert("RGB").resize((180, 80))
    imagel = image.convert("L")
    for i in range(0, image.height):
        for j in range(0, image.width):
            middle: tuple[int, int, int]
            print(color_it(image.getpixel((j, i))) + convert(imagel.getpixel((j, i))) + colorama.Style.RESET_ALL,
                  end='')
        print()
