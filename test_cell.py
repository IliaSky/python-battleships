import unittest
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
        self.assertTrue(self.cell_empty.is_empty())
        self.assertFalse(self.cell_string.is_empty())

    def test_is_full(self):
        self.assertFalse(self.cell_empty.is_full())
        self.assertTrue(self.cell_string.is_full())

    def test_empty(self):
        self.assertNotEqual(None, self.cell_string.contents)
        self.assertNotEqual(None, self.cell_ship.contents)
        self.cell_string.empty()
        self.cell_ship.empty()
        self.assertEqual(None, self.cell_string.contents)
        self.assertEqual(None, self.cell_ship.contents)

    def test_contains(self):
        self.assertTrue(Cell().contains(type(None)))
        self.assertTrue(Cell("something").contains(type("something")))

    def test_check_for_ship(self):
        self.assertTrue(self.cell_ship.check_for_ship())
        self.assertFalse(self.cell_empty.check_for_ship())
        self.assertFalse(self.cell_torpedo_net.check_for_ship())

    def test_hit(self):
        self.assertEqual("miss", self.cell_empty.hit())
        self.assertEqual("miss", self.cell_torpedo_net.hit())
        self.assertEqual("hit Andromeda", self.cell_ship.hit())

    def test_deploy_anti(self):
        self.cell_empty.deploy_anti("air")
        self.cell_ship.deploy_anti("radar")
        self.assertTrue(self.cell_empty.defence["air"])
        self.assertFalse(self.cell_empty.defence["radar"])
        self.assertFalse(self.cell_ship.defence["air"])
        self.assertTrue(self.cell_ship.defence["radar"])

    def test_radar_scan(self):
        self.cell_empty.deploy_anti("radar")
        self.cell_ship.deploy_anti("radar")
        self.assertEqual("jammed", self.cell_empty.radar_scan())
        self.assertEqual("empty", Cell().radar_scan())
        self.assertEqual("jammed", self.cell_ship.radar_scan())
        self.assertEqual("ship", self.cell_ship2.radar_scan())

    def test_air_strike(self):
        self.cell_empty.deploy_anti("air")
        self.cell_ship.deploy_anti("air")
        self.assertEqual("aircraft destroyed", self.cell_empty.air_strike())
        self.assertEqual("miss", Cell().air_strike())
        self.assertEqual("aircraft destroyed", self.cell_ship.air_strike())
        self.assertEqual("hit Millenium Falcon", self.cell_ship2.air_strike())

    def test_torpedo_hit(self):
        self.assertEqual("torpedo caught", self.cell_torpedo_net.torpedo_hit())
        self.assertEqual("miss", Cell().torpedo_hit())
        self.assertEqual("hit Millenium Falcon", self.cell_ship2.torpedo_hit())

    def test_set_torpedo_net(self):
        self.cell_empty.set_torpedo_net()
        self.assertTrue(self.cell_empty.contains(type(TorpedoNet())))

if __name__ == '__main__':
    unittest.main()
