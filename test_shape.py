import unittest
from shape import Shape
from vec2d import Vec2D


class TestShape(unittest.TestCase):

    def test_rotate(self):
        self.assertTrue(False)
        # todo - write this after fixing formula
        # self.assertEqual(expected, shape.rotate(rotation))

    def test_translate(self):
        shape = Shape([Vec2D(1, 1), Vec2D(1, 3)], Vec2D(1, 2))
        expected = Shape([Vec2D(2, 0), Vec2D(2, 2)], Vec2D(2, 1))
        self.assertEqual(expected.center,
                         shape.translate(Vec2D(1, -1)).center)
        self.assertEqual(expected.coords,
                         shape.translate(Vec2D(1, -1)).coords)

    def test_line(self):
        expected = [Vec2D(0, i) for i in range(5)]
        self.assertEqual(expected, Shape.line(5).coords)

    def test_square(self):
        expected = [Vec2D(0, 0), Vec2D(0, 1), Vec2D(1, 0), Vec2D(1, 1)]
        self.assertEqual(set(expected), set(Shape.square(2).coords))

if __name__ == '__main__':
    unittest.main()
