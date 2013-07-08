import unittest
from player import Player
from errors import InvalidPlayerPosition


class TestPlayer(unittest.TestCase):

    def test___init__(self):
        self.assertRaises(InvalidPlayerPosition, Player, 0)
        self.assertRaises(InvalidPlayerPosition, Player, 7)

    def test_add_ally(self):
        # not yet sure about this
        pass

if __name__ == '__main__':
    unittest.main()
