from collections import namedtuple


class Vec2D(namedtuple('Vec2D', 'x y')):

    def __add__(self, other):
        return Vec2D(self.x + other.x, self.y + other.y)

    def __neg__(self):
        return Vec2D(-self.x, -self.y)

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other):
        return Vec2D(self.x * other, self.y * other)

    def are_inside_world_with_size(self, size):
        return self.x in range(size) and self.y in range(size)


class WorldObject:
    pass


class Cell():

    def __init__(self, contents=None):
        if not isinstance(contents, (WorldObject, type(None))):
            raise TypeError
        self.contents = contents

    def is_empty(self):
        return self.contents is None

    def empty(self):
        self.contents = None

    def contains(self, type_):
        return isinstance(self.contents, type_)


class BattlefieldSide():

    def __init__(self, size):
        self.size = size
        self.matrix = [[Cell() for y in range(size)] for x in range(size)]

    def __len__(self):
        return self.size

    def __getitem__(self, key):
        if isinstance(key, Vec2D):
            return self.matrix[key.x][key.y]
        else:
            return self.matrix[key]


class Ship:

    def __init__(self, world, bow_coords, length, direction):
        self.world, self.length, self.direction = world, length, direction
        self.fuel = 0

        self.coords = [bow_coords - direction * i for i in range(length)]
        for coords in self.coords:
            self.world[bow_coords].contents = ShipPart(self)

        self.world[bow_coords].contents = ShipBow(self)


class ShipPart(WorldObject):

    def __init__(self, owner):
        self.owner = owner


class ShipBow(ShipPart):
    pass

