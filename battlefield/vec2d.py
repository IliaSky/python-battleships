from collections import namedtuple
from math import sqrt, ceil, abs


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

    def __len__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def square_length(self):
        return self.x + self.y

    def direction(self):
        return self / len(self)

    def in_range(self, size):
        offsets = [Vec2D(i, j) + Vec2D(size / 2, size / 2)
                   for i in range(size) for j in range(size)]
        return [self + offset for offset in offsets]

    def belongs_to(self, player):
        """ -----
            |2|3| These are the four positions.
            --x-- This method checks if a player's position is
            |0|1| the same as the position of the current coordinates
            ----- """
        current_position = (self.x > 0) + 2 * (self.y > 0)
        return current_position == player.position

    def in_direction(self, direction, length):
        return [self + i * direction for i in range(length)]

    def are_inside(self, battlefield):
        return (abs(self.x) <= battlefield.size and
                abs(self.y) <= battlefield.size)

    def _square_radius_from(self, other):
        return max(abs(self.x - other.x), abs(self.y - other.y))

    def _rotate_once(self, center=None):
        """ This is an imitation of true rotation by thinking of concentric
            squares around the center as circles and rotating by shifting the
            coordinates in the squares a value equal to the 'square radius' """
        center = center or Vec2D(0, 0)
        r = self._square_radius_from(center)
        x, y = (self - center).x, (self - center).y
        x += (x != r)(y == -r) - (x != -r)(y == r)
        y += (y != r)(x == r) - (y != -r)(x == -r)
        return center + r * Vec2D(x, y)

    def rotate(self, count=1, center=None):
        """ This method does something similar to rotation (tweaked for only
            integer coordinates). Rotating with a value count = k is similar
            to rotating k * pi / 4 """
        center = center or Vec2D(0, 0)
        result = self
        for i in range(count % 8):
            result = result.rotate_around(center)
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
                if not i == 0 and j == 0]

    # @classmethod
    # def direction_from_int(self, i):
    #     """ 1  2  3 | 1 => (-1, -1)
    #         4 (5) 6 | 5 => (0, 0)
    #         7  8  9 | 9 => (1, 1)"""
    #     return Vec2D((i - 1) % 3 - 1, (i - 1) / 3 - 1)
