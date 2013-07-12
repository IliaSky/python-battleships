from re import match
from colorama import init, Fore, Back, Style
from time import sleep
import os


from vec2d import Vec2D
from settings import Settings
from ui._getch import getch


init(autoreset=True)


def my_print(style, text=' '):
    print(style + text, end='')


def print_cell(cell, mouse_here=False):
    cls = match(r"<.*'.*?\.?([^\.]*)'>", str(type(cell.contents))).groups()[0]
    anti = cell.defence
    bg = [Back.BLACK, Back.GREEN, Back.BLUE, Back.CYAN][anti['air'] + 2 * anti['radar']]
    if mouse_here:
        bg = Back.MAGENTA
    bg += Fore.WHITE
    if cls == 'Terrain':
        my_print(bg, '^')
    if cls == 'NoneType':
        my_print(bg, ' ')
    if cls == 'ShipPart':
        my_print(bg + Fore.RED * cell.contents.is_hit,
                 Settings.SHIP_NAME_ABBR[cell.contents.owner.name])
    if cls == 'TorpedoNet':
        my_print(bg, 'n')


def battlefield_print(battlefield, mouse_coords=Vec2D(0, 0)):
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(battlefield.size.y * 2 + 1)[::-1]:
        for x in range(battlefield.size.x * 2 + 1):
            coords = Vec2D(x, y) - battlefield.size
            mouse_here = (mouse_coords == coords)
            if (coords.x == 0 or coords.y == 0):
                my_print([Back.WHITE, Back.MAGENTA][mouse_here])
            else:
                print_cell(battlefield[coords], mouse_here)
        print('')


