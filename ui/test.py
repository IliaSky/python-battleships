from re import match
from time import sleep
from colorama import init, Fore, Back, Style


from _getch import getch


init()


def my_print(style, text=' '):
    print(style + text, end='')


def print_cell(cell, mouse_here=False):
    cls = match(r"<.*'.*?\.?(.*)'>", str(type(cell.contents))).groups()[0]
    if mouse_here:
        bg = Back.MAGENTA
    if cls == 'Terrain':
        my_print(bg, '^')
    if cls == 'NoneType':
        my_print(bg, 'a')
    if cls == 'ShipPart':
        my_print(bg, 'cell.contents.id')
    if cls == 'TorpedoNet':
        my_print(bg, 'n')
    else:
        my_print(bg, 'sadsa')


class a:
    def __init__(self, contents=None):
        self.contents = contents


print_cell(a(), True)

# print(str(type(None)))
# print(match(r"<(class|type) '(?:.*\.)?(.*)'>", str(type(None))))
# print(match(r"<(?:class|type) '(?:.*\.)?(.*)'>", str(type(None))).groups()[0])
# print(match(r"<(?:class|type) '(?:.*\.)?(.*)'>", str(type(None))).groups()[0] == 'NoneType')
# print('a', end='')
# print('a', end='')
# print('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua sasa. ')
# print('/033[1;1H' + 'sasa')

# pos = lambda y, x: '\x1b[%d;%dH' % (y, x)
# # draw a white border.
# print(Back.WHITE, end='')
# print('%s%s' % (pos(3, 5), ' '*9), end='')
# for y in range(3, 1+7):
#     print('%s %s ' % (pos(y, 5), pos(y, 9)), end='')
# print('%s%s' % (pos(7, 5), ' '*9), end='')

# # display text on a Windows console
# # Windows XP with Python27 or Python32
# from ctypes import windll
# # needed for Python2/Python3 diff
# try:
#     input = raw_input
# except:
#     pass
# STD_OUTPUT_HANDLE = -11
# stdout_handle = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
# # look at the output and select the color you want
# # for instance hex E is yellow on black
# # hex 1E is yellow on blue
# # hex 2E is yellow on green and so on
# for color in range(0, 75):
#      windll.kernel32.SetConsoleTextAttribute(stdout_handle, color)
#      print("%X --> %s" % (color, "Have a fine day!"))
#      input("Press Enter to go on ... ")
