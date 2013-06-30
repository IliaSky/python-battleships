from collections import namedtuple
from math import sqrt, ceil


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
        return sqrt(self.x**2 + self.y**2)

    def square_length(self):
        return self.x + self.y

    def direction(self):
        return self / len(self)

    def in_range(self, size):
        offsets = [Vec2D(i, j) + Vec2D(size / 2, size / 2)
                   for i in range(size) for j in range(size)]
        return [self + offset for offset in offsets]


    def rotate(self, angle):
        """ rotates the vector, but only if the angle is a multiple of 90 """
        angle %= 360
        if angle == 90:
            return Vec2D(-self.y, self.x)
        elif angle == 270:
            return Vec2D(self.y, -self.x)
        elif angle == 180:
            return -self

    def belongs_to(self, player):
        """ -----
            |2|3| These are the four positions.
            --x-- This method checks if a player's position is
            |0|1| the same as the position of the current coordinates
            ----- """
        current_position = (self.x > 0) + 2 * (self.y > 0)
        return current_position == player.position
