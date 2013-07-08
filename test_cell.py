import unittest
from test_helper import must_be_true, must_be_false, must_be_equal
from cell import Cell
from misc import ShipPart, TorpedoNet


class MockShip:
    def __init__(self, name):
        self.name = name

    def hit(self):
        pass


class TestCell(unittest.TestCase):

    def setUp(self):
        self.cell_empty = Cell()
        self.cell_string = Cell("something")
        self.cell_ship = Cell(ShipPart(MockShip("Andromeda")))
        self.cell_ship2 = Cell(ShipPart(MockShip("Millenium Falcon")))
        self.cell_torpedo_net = Cell(TorpedoNet())

    def tearDown(self):
        self.cell_empty, self.cell_string = None, None
        self.cell_ship, self.torpedo_net = None, None

    def test_is_empty(self):
        must_be_true(self.cell_empty.is_empty())
        must_be_false(self.cell_string.is_empty())

    def test_is_full(self):
        must_be_false(self.cell_empty.is_full())
        must_be_true(self.cell_string.is_full())

    def test_empty(self):
        self.assertNotEqual(None, self.cell_string.contents)
        self.assertNotEqual(None, self.cell_ship.contents)
        self.cell_string.empty()
        self.cell_ship.empty()
        must_be_equal(None, self.cell_string.contents)
        must_be_equal(None, self.cell_ship.contents)

    def test_contains(self):
        must_be_true(Cell().contains(type(None)))
        must_be_true(Cell("something").contains(type("something")))

    def test_check_for_ship(self):
        must_be_true(self.cell_ship.check_for_ship())
        must_be_false(self.cell_empty.check_for_ship())
        must_be_false(self.cell_torpedo_net.check_for_ship())

    def test_hit(self):
        must_be_equal("miss", self.cell_empty.hit())
        must_be_equal("miss", self.cell_torpedo_net.hit())
        must_be_equal("hit Andromeda", self.cell_ship.hit())

    def test_deploy_anti(self):
        self.cell_empty.deploy_anti("air")
        self.cell_ship.deploy_anti("radar")
        must_be_true(self.cell_empty.defence["air"])
        must_be_false(self.cell_empty.defence["radar"])
        must_be_false(self.cell_ship.defence["air"])
        must_be_true(self.cell_ship.defence["radar"])

    def test_radar_scan(self):
        self.cell_empty.deploy_anti("radar")
        self.cell_ship.deploy_anti("radar")
        must_be_equal("jammed", self.cell_empty.radar_scan())
        must_be_equal("empty", Cell().radar_scan())
        must_be_equal("jammed", self.cell_ship.radar_scan())
        must_be_equal("ship", self.cell_ship2.radar_scan())

    def test_air_strike(self):
        self.cell_empty.deploy_anti("air")
        self.cell_ship.deploy_anti("air")
        must_be_equal("aircraft destroyed", self.cell_empty.air_strike())
        must_be_equal("miss", Cell().air_strike())
        must_be_equal("aircraft destroyed", self.cell_ship.air_strike())
        must_be_equal("hit Millenium Falcon", self.cell_ship2.air_strike())

    def test_torpedo_hit(self):
        must_be_equal("torpedo caught", self.cell_torpedo_net.torpedo_hit())
        must_be_equal("miss", Cell().torpedo_hit())
        must_be_equal("hit Millenium Falcon", self.cell_ship2.torpedo_hit())

    def test_set_torpedo_net(self):
        self.cell_empty.set_torpedo_net()
        must_be_true(self.cell_empty.contains(type(TorpedoNet())))

if __name__ == '__main__':
    unittest.main()
