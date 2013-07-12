import unittest
from test_helper import must_be_true, must_be_false, must_be_equal, must_raise
from misc import ShipPart


class MockShip:
    def __init__(self, name):
        self.name = name

    def hit(self):
        pass


class TestShipPart(unittest.TestCase):

    def setUp(self):
        self.ship_part = ShipPart(MockShip("X-Wing"))

    def tearDown(self):
        self.ship_part = None

    def test___init__(self):
        ship_part = ShipPart(5)
        must_be_equal(5, ship_part.owner)
        must_be_false(ship_part.is_hit)

    def test_hit(self):
        must_be_equal("hit X-Wing", self.ship_part.hit())

if __name__ == '__main__':
    unittest.main()
