import unittest
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
        self.assertEqual(5, ship_part.owner)
        self.assertFalse(ship_part._hit)

    def test_hit(self):
        self.assertEqual("hit X-Wing", self.ship_part.hit())

if __name__ == '__main__':
    unittest.main()
