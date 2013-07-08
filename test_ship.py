import unittest
from ship import Ship
from battlefield import Battlefield
from shape import Shape
from player import Player
from vec2d import Vec2D
from errors import NonDeployedShipTriesToAct


class TestShip(unittest.TestCase):

    def setUp(self):
        self.sea = Battlefield(Vec2D(6, 6))
        terrain = [Vec2D(1, 1), Vec2D(-1, -1)]
        self.sea2 = Battlefield(Vec2D(6, 6), terrain)
        self.ship = Ship("Battle Criuser", Shape.line(5))
        self.ship2 = Ship("Carrier", Shape.square(3))

    def tearDown(self):
        self.sea, self.ship, self.ship2 = None, None, None

    def test_can_be_deployed(self):
        is_false, is_true = self.assertFalse, self.assertTrue
        ship, ship2 = self.ship, self.ship2

        # cannot be deployed on enemy teritory
        is_false(ship.can_be_deployed(self.sea, Player(1), Vec2D(-1, 1)))

        # can be deployed on own teritory
        is_true(ship.can_be_deployed(self.sea, Player(1), Vec2D(1, 1)))
        is_true(ship2.can_be_deployed(self.sea, Player(3), Vec2D(-3, -3)))

        # cannot be deployed on terrain
        is_false(ship.can_be_deployed(self.sea2, Player(1), Vec2D(1, 1)))

    def test_fire_gun(self):
        self.assertRaises(NonDeployedShipTriesToAct,
                          self.ship.fire_gun, Vec2D(3, 3))
        self.ship.deploy(self.sea, Player(1), Vec2D(1, 1))
        self.ship2.deploy(self.sea, Player(3), Vec2D(-3, -3))
        self.assertEqual("miss", self.ship.fire_gun(Vec2D(-4, -4)))
        self.assertEqual("hit Carrier", self.ship.fire_gun(Vec2D(-2, -2)))

    def test_hit(self):
        self.ship.deploy(self.sea, Player(1), Vec2D(1, 1))
        self.assertEqual("hit Battle Criuser", self.sea[Vec2D(1, 1)].hit())

    def test_parts_coords(self):
        self.ship2.deploy(self.sea, Player(3), Vec2D(-3, -3))
        expected = set([Vec2D(-3, -3), Vec2D(-3, -2), Vec2D(-3, -1),
                        Vec2D(-2, -3), Vec2D(-2, -2), Vec2D(-2, -1),
                        Vec2D(-1, -3), Vec2D(-1, -2), Vec2D(-1, -1)])
        self.assertEqual(expected, set(self.ship2.parts_coords()))

    def test_undeploy(self):
        self.ship2.deploy(self.sea, Player(3), Vec2D(-3, -3))
        self.ship2.undeploy()
        self.assertTrue(self.sea[Vec2D(-3, -3)].is_empty())

if __name__ == '__main__':
    unittest.main()
