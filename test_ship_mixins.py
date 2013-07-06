import unittest
from ship_mixins import *


class TestMovableMixin(unittest.TestCase):

    def test_move(self):
        expected = None
        movable_mixin = MovableMixin()
        self.assertEqual(expected, movable_mixin.move(battlefield, coords,
        rotation))

    def test_move_cost(self):
        expected = None
        movable_mixin = MovableMixin()
        self.assertEqual(expected, movable_mixin.move_cost(coords, rotation))


class TestRadarMixin(unittest.TestCase):

    def test_scan(self):
        expected = None
        radar_mixin = RadarMixin()
        self.assertEqual(expected, radar_mixin.scan(battlefield, coords))


class TestAirStrikeMixin(unittest.TestCase):

    def test_air_strike(self):
        expected = None
        air_strike_mixin = AirStrikeMixin()
        self.assertEqual(expected, air_strike_mixin.air_strike(battlefield,
        coords, direction))


class TestTorpedoMixin(unittest.TestCase):

    def test_torpedo(self):
        expected = None
        torpedo_mixin = TorpedoMixin()
        self.assertEqual(expected, torpedo_mixin.torpedo(battlefield, coords,
        direction))


class TestRadarJamMixin(unittest.TestCase):

    def test_radar_jam(self):
        expected = None
        radar_jam_mixin = RadarJamMixin()
        self.assertEqual(expected, radar_jam_mixin.radar_jam(battlefield,
        coords))


class TestAntiAirMixin(unittest.TestCase):

    def test_deploy_anti_air(self):
        expected = None
        anti_air_mixin = AntiAirMixin()
        self.assertEqual(expected,
        anti_air_mixin.deploy_anti_air(battlefield, coords))


class TestTorpedoNetMixin(unittest.TestCase):

    def test_torpedo_net(self):
        expected = None
        torpedo_net_mixin = TorpedoNetMixin()
        self.assertEqual(expected, torpedo_net_mixin.torpedo_net(battlefield,
        coords, direction))

if __name__ == '__main__':
    unittest.main()
