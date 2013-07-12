import unittest
from test_helper import must_be_true, must_be_false, must_be_equal, must_raise
from shape import Shape, line, square
from vec2d import Vec2D


class TestShape(unittest.TestCase):

    def test_rotate(self):
        shape = Shape([Vec2D(1, 1), Vec2D(1, 3)], Vec2D(1, 2))
        shape2 = Shape([Vec2D(1, 1), Vec2D(1, 3)], Vec2D(1, 2))
        must_be_equal(set(shape2), set(shape.rotate(4)))

    def test_translate(self):
        shape = Shape([Vec2D(1, 1), Vec2D(1, 3)], Vec2D(1, 2))
        expected = Shape([Vec2D(2, 0), Vec2D(2, 2)], Vec2D(2, 1))
        must_be_equal(expected.center, shape.translate(Vec2D(1, -1)).center)
        must_be_equal(expected.coords, shape.translate(Vec2D(1, -1)).coords)

    def test_line(self):
        expected = [Vec2D(i, 0) for i in range(5)]
        must_be_equal(expected, line(5).coords)

    def test_square(self):
        expected = [Vec2D(0, 0), Vec2D(0, 1), Vec2D(1, 0), Vec2D(1, 1)]
        must_be_equal(set(expected), set(square(2).coords))

if __name__ == '__main__':
    unittest.main()
