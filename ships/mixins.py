from math import ceil


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
    pass


class RadarJamMixin:
    pass


class TorpedoMixin:
    pass


class TorpedoNetMixin:
    pass


class AirAttackMixin:
    pass


class AntiAirMixin:
    pass
