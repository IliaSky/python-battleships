import unittest
from test_helper import must_be_true, must_be_false, must_be_equal, must_raise
from game import Game
from player import Player
from shape import Shape
from ship import Ship
from battlefield import Battlefield
from vec2d import Vec2D


class TestGame(unittest.TestCase):

    def setUp(self):
        battlefield = Battlefield(Vec2D(4, 4))
        players = [Player(1), Player(3)]
        available_fleets = {"one ship": [Ship('a', Shape.line(3))]}
        self.game = Game(battlefield, players, available_fleets)

    def tearDown(self):
        self.game = None

    def test_alive_players(self):
        pass

    def test_is_in_progress(self):
        pass

    def test_prepare_fleets(self):
        pass

    def test_start(self):
        pass

if __name__ == '__main__':
    unittest.main()
