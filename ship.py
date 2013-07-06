from misc import ShipPart
from errors import *
from settings import Settings


def check_action(fn):
    def checked(self, *args):
        action_name = fn.__name__()
        resourse_name = Settings.resourse(action_name)

        if not hasattr(self.actions, action_name):
            raise InvalidShipAction

        if not hasattr(self.misc, resourse_name):
            return self.fn(*args)

        if self.misc[action_name] <= 0:
            raise InsufficientAmmunition

        self.misc[action_name] -= 1
        return self.fn(*args)
    return checked


class Ship:

    def __init__(self, name, player, shape,
                 actions=["fire_gun", "move"], misc={"fuel": 0},
                 action_shapes={}):
        self.name, self.player, self.shape = name, player, shape
        self.hp = len(shape)
        self.parts = [ShipPart(self) for i in range(len(self))]

        for key, value in additional.items():
            self.__dict__[key] = value

    def __len__(self):
        return len(self.shape)

    def fire_gun(self, coords):
        if not hasattr(self, 'battlefield'):
            raise NonDeployedShipTriesToAct
        return self.battlefield[coords].hit()

    @check_action
    def fire_battery(self, coords, rotation=0):
        pass

    def action_shape(self, action_name):
        pass

    def can_be_deployed(self, battlefield, start_coords, rotation=0):
        if rotation % 2 != 0:
            return False

        for coords in self.shape.translate(start_coords).rotate(rotation):
            if not coords.belong_to(self.player) or battlefield[coords].is_full():
                return False

        return True

    def deploy(self, battlefield, coords, rotation=0):
        if not self.can_be_deployed(battlefield, coords, rotation):
            raise CannotDeployShip

        self.battlefield, self.coords = battlefield, coords
        self.shape.rotate(rotation)

        for coords, part in zip(self.parts_coords(), self.parts):
            battlefield[coords] = part

    def undeploy(self):
        for coords, part in zip(self.parts_coords(), self.parts):
            self.battlefield[coords] = None

    def parts_coords(self):
        return self.shape.translate(self.coords)

    def hit(self):
        self.hp -= 1
        if self.hp <= 0:
            self.destroy()

    def destroy(self):
        pass

    def move(self, coords, rotation=0):
        old_coords = self.coords
        self.undeploy()
        if (self._can_be_moved()):
            self.deploy(self.battlefield, coords, rotation)
        else:
            self.deploy(self.battlefield, old_coords)
            raise CannotDeployShip

    def _can_be_moved(self, coords, rotation=0):
        return (self._move_cost(coords, rotation) <= self.fuel and
                self.can_be_deployed(self.battlefield, coords, rotation))

    def _move_cost(self, coords, rotation):
        return len(self.coords - coords) + self._rotate_cost(rotation)

    def _rotate_cost(self, rotation):
        """ Ships can only be rotated by 90, 180, 270 degrees
            In ingame rotation units those are 2, 4 and 6
            2(90deg), 6(270deg) => 1; 4(180deg) => 2 """
        return (rotation / 2 % 4 - 1) % 2 + 1

    @check_action
    def scan(self, coords):
        return [self.battlefield[i].radar_scan() for i in coords.in_range(3)]

    @check_action
    def air_strike(self, coords, direction):
        return [self.battlefield[i].air_strike()
                for i in coords.in_direction(direction, 3)]

    @check_action
    def torpedo(self, coords, direction):
        torpedo_trail = []
        coords += direction
        while (coords.are_inside(self.battlefield) and
               self.battlefield[coords].is_empty()):
            torpedo_trail.append(self.battlefield[coords].torpedo_hit())
            coords += direction
        torpedo_trail.append(self.battlefield[coords].torpedo_hit())
        return torpedo_trail

    @check_action
    def radar_jam(self, coords, rotation=0):
        shape = Settings.shape("radar_jam").rotate(rotation)
        for i in shape.translate(coords):
            self.battlefield[i].deploy_anti("radar")

    @check_action
    def deploy_anti_air(self, coords, rotation=0):
        shape = Settings.shape("torpedo_net").rotate(rotation)
        for i in shape("anti_air").translate(coords):
            self.battlefield[i].deploy_anti("air")

    @check_action
    def torpedo_net(self, coords, rotation=0):
        shape = Settings.shape("torpedo_net").rotate(rotation)
        for i in shape.translate(coords):
            self.battlefield[i].set_torpedo_net()
