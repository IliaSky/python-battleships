import unittest


from test_helper import must_raise
from player import Player
from errors import InvalidPlayerPosition


class TestPlayer(unittest.TestCase):

    def test___init__(self):
        must_raise(InvalidPlayerPosition, Player, 0)
        must_raise(InvalidPlayerPosition, Player, 7)

    def test_add_ally(self):
        # not yet sure about this
        pass

if __name__ == '__main__':
    unittest.main()
