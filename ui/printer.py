from re import match
from _getch import getch
from colorama import init, Fore, Back, Style
from time import sleep


init(autoreset=True)


SYMBOLS = {
    'ship': ''
}


def my_print(style, text=' '):
    print(style + text, end='')


def print_cell(cell, mouse_here=False):
    cls = match(r"<.*'.*\.?(.*)'>", str(type(cell.contents))).groups()[0]
    anti = cell.defence
    bg = [Back.GREEN, Back.BLUE, Back.CYAN][anti['air'] + 2 * anti['radar']]
    if mouse_here:
        bg = Back.MAGENTA
    if cls == 'Terrain':
        my_print(bg, '^')
    if cls == 'NoneType':
        my_print(bg, ' ')
    if cls == 'ShipPart':
        # print('x' if obj.is_hit() else obj.id)
        my_print(bg + Fore.RED * cell.contents.is_hit(), cell.contents.id)
    if cls == 'TorpedoNet':
        my_print(bg, 'n')


def battlefield_print(battlefield, mouse_coords):
    for y in battlefield.size.y * 2 + 1:
        for x in battlefield.size.x * 2 + 1:
            mouse_here = (Vec2D(x, y) == mouse_coords)
            if ((Vec2D(x, y) - battlefield.size).quadrant == 0):
                my_print(Back.MAGENTA if mouse_here else Back.YELLOW)
            else:
                print_cell(battlefield[Vec2D(x, y)], mouse_here)
        print('')


def function():
    pass

    # cls = match(r".*\.(.*)'>", str(type(obj))).groups()[1]
    # cls = search(r"(?<=\.)(.*)(?='>)", str(type(obj))).groups()[0]


q=not match(r"<.*'.*\.?(.*)'>", str(type(None))).groups()[0] == 'NoneType'
# print(match(r".*'(.*)'>", str(type(None))).groups()[0] == 'NoneType')
print(Fore.RED*False + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL+"sas"+Back.GREEN + Style.RESET_ALL+"sas"+Back.GREEN + Fore.RED + Style.RESET_ALL+"sas")
print('back to normal now')
sleep(10)

