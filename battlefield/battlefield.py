from cell import Cell
from misc import Terrain
from errors import CannotDeployShip


class Battlefield():

    def __init__(self, size, terrain_coords=[]):
        self.size = size
        self.ships = []
        width, height = 2 * size.x, 2 * size.y
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
        if ship.can_be_deployed(self, coords, rotation):
            ship.deploy(self, coords, rotation)
            self.ships.append(ship)
        else:
            raise CannotDeployShip

