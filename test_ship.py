import unittest
from test_helper import must_be_true, must_be_false, must_be_equal, must_raise
from ship import Ship
from battlefield import Battlefield
from shape import line, square
from player import Player
from vec2d import Vec2D
from errors import NonDeployedShipTriesToAct


class TestShip(unittest.TestCase):

    def setUp(self):
        self.sea = Battlefield(Vec2D(6, 6))
        terrain = [Vec2D(1, 1), Vec2D(-1, -1)]
        self.sea2 = Battlefield(Vec2D(6, 6), terrain)
        self.ship = Ship("Battle Criuser", line(5))
        self.ship2 = Ship("Carrier", square(3))

    def tearDown(self):
        self.sea, self.ship, self.ship2 = None, None, None

    def test_can_be_deployed(self):
        ship, ship2, sea, sea2 = self.ship, self.ship2, self.sea, self.sea2

        # cannot be deployed on enemy teritory
        must_be_false(ship.can_be_deployed(sea, Player(1), Vec2D(-1, 1)))

        # can be deployed on own teritory
        must_be_true(ship.can_be_deployed(sea, Player(1), Vec2D(1, 1)))
        must_be_true(ship2.can_be_deployed(sea, Player(3), Vec2D(-3, -3)))

        # cannot be deployed on terrain
        must_be_false(ship.can_be_deployed(sea2, Player(1), Vec2D(1, 1)))

    def test_fire_gun(self):
        must_raise(NonDeployedShipTriesToAct, self.ship.fire_gun, Vec2D(3, 3))
        self.ship.deploy(self.sea, Player(1), Vec2D(1, 1))
        self.ship2.deploy(self.sea, Player(3), Vec2D(-3, -3))
        must_be_equal("miss", self.ship.fire_gun(Vec2D(-4, -4)))
        must_be_equal("hit Carrier", self.ship.fire_gun(Vec2D(-2, -2)))

    def test_hit(self):
        self.ship.deploy(self.sea, Player(1), Vec2D(1, 1))
        must_be_equal("hit Battle Criuser", self.sea[Vec2D(1, 1)].hit())

    def test_parts_coords(self):
        self.ship2.deploy(self.sea, Player(3), Vec2D(-3, -3))
        expected = set([Vec2D(-3, -3), Vec2D(-3, -2), Vec2D(-3, -1),
                        Vec2D(-2, -3), Vec2D(-2, -2), Vec2D(-2, -1),
                        Vec2D(-1, -3), Vec2D(-1, -2), Vec2D(-1, -1)])
        must_be_equal(expected, set(self.ship2.parts_coords()))

    def test_undeploy(self):
        self.ship2.deploy(self.sea, Player(3), Vec2D(-3, -3))
        self.ship2.undeploy()
        must_be_true(self.sea[Vec2D(-3, -3)].is_empty())

if __name__ == '__main__':
    unittest.main()
