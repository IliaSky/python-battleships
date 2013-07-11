from re import match
from colorama import init, Fore, Back, Style
from time import sleep
import os


from ui._getch import getch
from vec2d import Vec2D


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
        # print('x' if obj.is_hit() else obj.id)
        my_print(bg + Fore.RED * cell.contents.is_hit, str(cell.contents.owner.id + 1))
    if cls == 'TorpedoNet':
        my_print(bg, 'n')


def battlefield_print(battlefield, mouse_coords=Vec2D(0, 0)):
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(battlefield.size.y * 2 + 1)[::-1]:
        for x in range(battlefield.size.x * 2 + 1):
            coords = Vec2D(x, y) - battlefield.size
            mouse_here = (mouse_coords == coords)
            if (coords.x == 0 or coords.y == 0):
                my_print([Back.BLUE, Back.MAGENTA][mouse_here])
            else:
                print_cell(battlefield[coords], mouse_here)
        print('')


def function():
    print('Lorem')

    # cls = match(r".*\.(.*)'>", str(type(obj))).groups()[1]
    # cls = search(r"(?<=\.)(.*)(?='>)", str(type(obj))).groups()[0]


# q=not match(r"<.*'.*\.?(.*)'>", str(type(None))).groups()[0] == 'NoneType'
# # print(match(r".*'(.*)'>", str(type(None))).groups()[0] == 'NoneType')
# print(Fore.RED*False + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL+"sas"+Back.GREEN + Style.RESET_ALL+"sas"+Back.GREEN + Fore.RED + Style.RESET_ALL+"sas")
# print('back to normal now')
# sleep(10)

