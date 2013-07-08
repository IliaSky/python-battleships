from cell import Cell
from misc import Terrain


class Battlefield():

    def __init__(self, size, terrain_coords=[]):
        """ Creates a battlefield, which has 4 areas (the four quadrants).
            The size given is a vector, containing the biggest north-east
            coordinates that will be available."""
        self.size = size
        self.ships = []
        width, height = 2 * size.x + 1, 2 * size.y + 1
        self.matrix = [[Cell() for x in range(width)] for y in range(height)]
        for coords in terrain_coords:
            self[coords] = Terrain()

    def __getitem__(self, key):
        key += self.size
        return self.matrix[key.y][key.x]

    def __setitem__(self, key, value):
        key += self.size
        self.matrix[key.y][key.x] = Cell(value)

    def __contains__(self, coords):
        """ Checks if the coordinates are inside the battlefield
            Note that the axises (with either x or y equal to zero)
            are not considered part of the battlefield """
        x, y = abs(coords.x), abs(coords.y)
        width, height = self.size.x, self.size.y
        return x <= width and y <= height and x != 0 and y != 0

    def print(self):
        pass
