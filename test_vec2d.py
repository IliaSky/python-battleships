import unittest
from test_helper import must_be_true, must_be_false, must_be_equal, must_raise
from vec2d import Vec2D
from battlefield import Battlefield
from errors import DirectionNotSupported


class TestVec2D(unittest.TestCase):

    def test___add__(self):
        must_be_equal(Vec2D(4, 4), Vec2D(3, 3).__add__(Vec2D(1, 1)))

    def test___div__(self):
        must_be_equal(Vec2D(1, 1), Vec2D(3, 3).__div__(3))

    def test___len__(self):
        must_be_equal(3, Vec2D(3, 2).__len__())
        must_be_equal(5, Vec2D(-3, 5).__len__())
        must_be_equal(4, Vec2D(1, -4).__len__())
        must_be_equal(7, Vec2D(-7, -2).__len__())

    def test___mul__(self):
        must_be_equal(Vec2D(-6, -6), Vec2D(3, 3).__mul__(-2))

    def test___neg__(self):
        must_be_equal(Vec2D(-3, -3), Vec2D(3, 3).__neg__())

    def test___sub__(self):
        must_be_equal(Vec2D(1, -4), Vec2D(3, 3).__sub__(Vec2D(2, 7)))

    def test_quadrant(self):
        must_be_equal(0, Vec2D(1, 0).quadrant())
        must_be_equal(0, Vec2D(0, -1).quadrant())
        must_be_equal(1, Vec2D(1, 1).quadrant())
        must_be_equal(2, Vec2D(-5, 3).quadrant())
        must_be_equal(3, Vec2D(-9, -200).quadrant())
        must_be_equal(4, Vec2D(2, -1).quadrant())

    def test_direction(self):
        must_be_equal(Vec2D(1, 1), Vec2D(3, 3).direction())
        must_be_equal(Vec2D(-1, 1), Vec2D(-3, 3).direction())
        must_be_equal(Vec2D(-1, 0), Vec2D(-3, 0).direction())
        must_raise(ArithmeticError, Vec2D(0, 0).direction)
        must_raise(DirectionNotSupported, Vec2D(2, 1).direction)

    def test_directions(self):
        directions = [Vec2D(-1, -1), Vec2D(-1, 0), Vec2D(-1, 1), Vec2D(0, -1),
                      Vec2D(0, 1), Vec2D(1, -1), Vec2D(1, 0), Vec2D(1, 1)]
        must_be_equal(set(directions), set(Vec2D.directions()))

    def test_in_direction(self):
        line = [Vec2D(3, 3), Vec2D(4, 2), Vec2D(5, 1)]
        must_be_equal(line, Vec2D(3, 3).in_direction(Vec2D(1, -1), 3))

    def test_in_range(self):
        square_1 = [Vec2D(3, 3)]
        square_2 = [Vec2D(4, 4), Vec2D(4, 5), Vec2D(5, 4), Vec2D(5, 5)]
        square_3 = [Vec2D(4, 4), Vec2D(4, 5), Vec2D(4, 6), Vec2D(5, 4),
                    Vec2D(5, 5), Vec2D(5, 6), Vec2D(6, 4), Vec2D(6, 5),
                    Vec2D(6, 6)]
        must_be_equal(square_1, Vec2D(3, 3).in_range(1))
        must_be_equal(square_2, Vec2D(3, 3).in_range(2))
        must_be_equal(square_3, Vec2D(3, 3).in_range(3))

    def test_rotate_once(self):
        # todo - some more tests here
        must_be_equal(Vec2D(0, 3), Vec2D(3, 3).rotate_once())

if __name__ == '__main__':
    unittest.main()
