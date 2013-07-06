import unittest
from game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.battlefield = Battlefield(4)

    def tearDown(self):
        self.battlefield = None

    def test___init__(self):
        expected = None
        game = Game(battlefield, players, available_fleets)

    def test_alive_players(self):
        expected = None
        game = Game(battlefield, players, available_fleets)
        self.assertEqual(expected, game.alive_players())

    def test_is_in_progress(self):
        expected = None
        game = Game(battlefield, players, available_fleets)
        self.assertEqual(expected, game.is_in_progress())

    def test_start(self):
        expected = None
        game = Game(battlefield, players, available_fleets)
        self.assertEqual(expected, game.start())

if __name__ == '__main__':
    unittest.main()
