from collections import namedtuple
from math import sqrt


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

    def direction(self):
        return self / len(self)

    def belongs_to_player(self, player):
        """ -----
            |2|3| These are the four positions.
            --x-- This method checks if a player's position is
            |0|1| the same as the position of the current coordinates
            ----- """
        current_position = (self.x > 0) + 2 * (self.y > 0)
        return current_position == player.position
