import unittest


from test_helper import must_be_true, must_be_false
from battlefield import Battlefield
from vec2d import Vec2D


class TestBattlefield(unittest.TestCase):

    def test___contains__(self):
        battlefield = Battlefield(Vec2D(3, 3))
        must_be_true(Vec2D(2, 3)in battlefield)
        must_be_true(Vec2D(-3, 1) in battlefield)
        must_be_false(Vec2D(0, 0) in battlefield)
        must_be_false(Vec2D(3, 7) in battlefield)


if __name__ == '__main__':
    unittest.main()
