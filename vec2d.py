from collections import namedtuple
from fractions import gcd
from re import match


from errors import DirectionNotSupported, InvalidCoordinates


class Vec2D(namedtuple('Vec2D', 'x y')):

    def __add__(self, other):
        return Vec2D(self.x + other.x, self.y + other.y)

    def __neg__(self):
        return Vec2D(-self.x, -self.y)

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other):
        return Vec2D(self.x * other, self.y * other)

    def __div__(self, other):
        return Vec2D(self.x / other, self.y / other)

    def __str__(self):
        return "({1}, {2})".format(str(self.x), str(self.y))

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        """ Returns max(abs(x),abs(y)) instead of actual length
            This is the number of single moves or diagonal ones
            needed to get to those coordinates from the center """
        return max(abs(self.x), abs(self.y))

    def square_length(self):
        return abs(self.x) + abs(self.y)

    def quadrant(self):
        """ |2|1| These are the quadrants known from math.
            |3|4| Returns 0 if the coordinates belongs to an axis"""
        if self.x == 0 or self.y == 0:
            return 0
        return 2 + 2 * (self.y < 0) - (self.y * self.x > 0)

    def belong_to(self, player):
        """ Checks if the coordinates are in the player's quadrant """
        return self.quadrant() == player.position

    def direction(self):
        """ Returns direction of the vector from Vec2D.directions
            Raises exceptions if the direction is not one of those """
        if self.x == 0 and self.y == 0:
            # return Vec2D(0, 0)
            raise ArithmeticError("Cannot compute direction of zero vector")
        if self.x == 0 or self.y == 0 or self.x ** 2 - self.y ** 2 == 0:
            return self.__div__(abs(gcd(self.x, self.y)))
        raise DirectionNotSupported("Direction not in Vec2D.directions")

    def in_direction(self, direction, n):
        """ Returns a list of the next n coordinates in the direction """
        return [self + direction * i for i in range(n)]

    def in_range(self, size):
        """ Returns a list all the coordinates in a square with a current side
            length(size) with the current Vec2D as it's center.
            Note: the square is always made up of int coordinates, so if the
            side size is even then the square is translated by (0.5, 0.5) """
        offsets = [Vec2D(i, j) + Vec2D(size // 2, size // 2)
                   for i in range(size) for j in range(size)]
        return [self + offset for offset in offsets]

    def rotate_once(self, center=None):
        """ This is an imitation of true rotation by thinking of concentric
            squares around the center as circles and rotating by shifting the
            coordinates in the squares a value equal to the 'square radius' """
        center = center or Vec2D(0, 0)
        x, y, r = (self - center).x, (self - center).y, len(self - center)
        move_x = (x != r) * (y == -r) - (x != -r) * (y == r)
        move_y = (y != r) * (x == r) - (y != -r) * (x == -r)
        return center + Vec2D(move_x, move_y) * r
        # if y == -r and x != r:
        #     y += x
        #     x += r
        #     # return center + Vec2D(min(r, x + r), max(0, x))
        # elif x == r and y != r:
        #     # y += x * (x > 0)
        #     x = min(r, r - y)
        #     y = min(r, r + y)
        #     # return center + Vec2D(-max(0, y), min(r, x + r))
        # elif y == r and x != -r:
        #     y = min(r, r + x)
        #     x = max(-r, x - r)
        #     # return center + Vec2D(max(-r, x - r), -min(0, x))
        # elif x == -r and y != -r:

        #     # return center + Vec2D(max(-r), max(0, x))
        # return center + offset.between(-r, r)
        # todo - fix formula

    # def between(self, a, b):
    #     return Vec2D(max(a, min(b, self.x)), max(a, min(b, self.y)))

    def rotate(self, count=1, center=None):
        """ This method does something similar to rotation (tweaked for only
            integer coordinates). Rotating with a value count = k is similar
            to rotating k * pi / 4 """
        center = center or Vec2D(0, 0)
        result = self
        for i in range(count % 8):
            result = result.rotate_once(center)
        return result

    # def simple_rotate(self, angle):
    #     """ rotates the vector, but only if the angle is a multiple of 90 """
    #     angle %= 360
    #     if angle == 90:
    #         return Vec2D(-self.y, self.x)
    #     elif angle == 270:
    #         return Vec2D(self.y, -self.x)
    #     elif angle == 180:
    #         return -self

    @classmethod
    def directions(cls):
        return [Vec2D(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1]
                if i != 0 or j != 0]

    @classmethod
    def parse(cls, string):
        # m = match(r'\(?(-?[0-9]*),? (-?[0-9]*)\)?', string)
        m = match(r'(-?[0-9]) (-?[0-9])', string)
        if m is None:
            raise InvalidCoordinates(string)
        return Vec2D(int(m.groups()[0]), int(m.groups()[1]))

    # @classmethod
    # def direction_from_int(self, i):
    #     """ 1  2  3 | 1 => (-1, -1)
    #         4 (5) 6 | 5 => (0, 0)
    #         7  8  9 | 9 => (1, 1)"""
    #     return Vec2D((i - 1) % 3 - 1, (i - 1) / 3 - 1)
# print(Vec2D.parse("111"))
