from cell import Cell
from misc import Terrain
from errors import CannotDeployShip


class Battlefield():

    def __init__(self, size, terrain_coords=[]):
        """ Creates a battlefield, which has 4 areas,
            each one belonging to one player. The areas are the four quadrants"""
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

    def deploy_ship(self, ship, coords, rotation):
        ship.deploy(self, coords, rotation)
        self.ships.append(ship)
