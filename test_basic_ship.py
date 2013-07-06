import unittest
from basic_ship import BasicShip
from battlefield import Battlefield
from shape import Shape
from player import Player
from vec2d import Vec2D
from errors import NonDeployedShipTriesToAct


class TestBasicShip(unittest.TestCase):

    def setUp(self):
        self.sea = Battlefield(Vec2D(6, 6))
        terrain = [Vec2D(1, 1), Vec2D(-1, -1)]
        self.sea2 = Battlefield(Vec2D(6, 6), terrain)
        self.ship = BasicShip("Battle Criuser", Player(1), Shape.line(5))
        self.ship2 = BasicShip("Carrier", Player(3), Shape.square(3))

    def tearDown(self):
        self.sea, self.ship, self.ship2 = None, None, None

    def test_can_be_deployed(self):
        # todo - fix rotation formula before more tests here
        self.assertFalse(self.ship.can_be_deployed(self.sea, Vec2D(-1, 1)))
        self.assertTrue(self.ship.can_be_deployed(self.sea, Vec2D(1, 1)))
        self.assertFalse(self.ship.can_be_deployed(self.sea2, Vec2D(1, 1)))
        self.assertTrue(self.ship.can_be_deployed(self.sea2, Vec2D(2, 2)))
        self.assertTrue(self.ship2.can_be_deployed(self.sea, Vec2D(-3, -3)))

    def test_fire_gun(self):
        self.assertRaises(NonDeployedShipTriesToAct,
                          self.ship.fire_gun, Vec2D(3, 3))
        self.ship.deploy(self.sea, Vec2D(1, 1))
        self.ship2.deploy(self.sea, Vec2D(-3, -3))
        self.assertEqual("miss", self.ship.fire_gun(Vec2D(-4, -4)))
        self.assertEqual("hit Carrier", self.ship.fire_gun(Vec2D(-2, -2)))

    def test_hit(self):
        self.ship.deploy(self.sea, Vec2D(1, 1))
        self.assertEqual("hit Battle Criuser", self.sea[Vec2D(1, 1)].hit())

    def test_parts_coords(self):
        self.ship2.deploy(self.sea, Vec2D(-3, -3))
        expected = set([Vec2D(-3, -3), Vec2D(-3, -2), Vec2D(-3, -1),
                        Vec2D(-2, -3), Vec2D(-2, -2), Vec2D(-2, -1),
                        Vec2D(-1, -3), Vec2D(-1, -2), Vec2D(-1, -1)])
        self.assertEqual(expected, set(self.ship2.parts_coords()))

    # def test_rotate(self):
    #     expected = None
    #     basic_ship = BasicShip(player, shape, additional)
    #     self.assertEqual(expected, basic_ship.rotate(rotation))

    def test_undeploy(self):
        self.ship2.deploy(self.sea, Vec2D(-3, -3))
        self.ship2.undeploy()
        self.assertTrue(self.sea[Vec2D(-3, -3)].is_empty())

if __name__ == '__main__':
    unittest.main()
