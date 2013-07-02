from math import ceil
from errors import CannotDeployShip


class MovableMixin:
    def move(self, battlefield, coords, rotation):
        old_coords = self.coords
        self.undeploy()
        if (self.move_cost(coords, rotation) <= self.fuel and
           self.can_be_deployed(battlefield, coords, rotation)):
            self.deploy(battlefield, coords, rotation)
        else:
            self.deploy(battlefield, old_coords)
            raise CannotDeployShip

    def move_cost(self, coords, rotation):
        return ceil(len(self) * (self._move_cost(coords) / 3 +
                                 self._rotate_cost(rotation)))

    def _move_cost(self, coords):
        return len(self.coords - coords)

    def _rotate_cost(self, rotation):
        """ 90, 270 => 1; 180 => 2 """
        return (rotation / 90 % 4 - 1) % 2 + 1


class RadarMixin:
    def scan(self, battlefield, coords):
        return [battlefield[i].radar_scan() for i in coords.in_range(3)]


class AirStrikeMixin:
    def air_strike(self, battlefield, coords, direction):
        return [battlefield[i].air_strike()
                for i in coords.in_direction(direction, 3)]


class TorpedoMixin:
    def torpedo(self, battlefield, coords, direction):
        self.torpedos -= 1
        torpedo_trail = []
        coords += direction
        while coords.are_inside(battlefield) and battlefield[coords].is_empty():
            torpedo_trail.append(battlefield[coords].torpedo_hit())
            coords += direction
        torpedo_trail.append(battlefield[coords].torpedo_hit())
        return torpedo_trail


class RadarJamMixin:
    def radar_jam(self, battlefield, coords):
        for i in coords.in_range(4):
            battlefield[i].deploy_anti("radar")


class AntiAirMixin:
    def deploy_anti_air(self, battlefield, coords):
        for i in coords.in_range(4):
            battlefield[i].deploy_anti("air")


class TorpedoNetMixin:
    def torpedo_net(self, battlefield, coords, direction):
        for i in coords.in_direction(direction, 3):
            battlefield[i].set_torpedo_net()
