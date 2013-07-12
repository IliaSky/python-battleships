from misc import ShipPart
from errors import *
from settings import Settings


def check_action(fn):
    def checked(self, *args):
        action_name = fn.__name__
        resourse_name = Settings.RESOURSES[action_name]

        if not hasattr(self, 'battlefield'):
            raise NonDeployedShipTriesToAct

        if resourse_name not in self.resourses.keys():
            print(resourse_name)
            print(self.resourses.keys())
            raise InvalidCommand('Chosen ship cannot perform this action')

        if self.resourses[resourse_name] == 0:
            raise InvalidCommand('Chosen ship does not have enough resources')

        # if not Settings.shape(action_name) in self.battlefield:
        #     raise InvalidCommand('Chosen coords are outside the battlefield')

        if self.resourses[resourse_name] == -1:
            return fn(self, *args)

        self.resourses[resourse_name] -= 1
        return fn(self, *args)
    return checked


class Ship:

    def __init__(self, name, shape, resourses={"fuel": 10, "gun_shots": -1}):
        """ Creates an instance of a ship.
            By default ships have 10 fuel unless stated otherwise """
        self.name, self.shape, self.hp = name, shape, len(shape)
        self.resourses = {"fuel": 10, "gun_shots": -1}
        self.resourses.update(resourses)
        self.parts = [ShipPart(self) for i in range(len(self))]

    def __len__(self):
        return len(self.shape)

    def __str__(self):
        return self.name + " with " + str(self.resourses)

    def __repr__(self):
        return '<{}>'.format(str(self))

    @check_action
    def fire_gun(self, coords):
        return self.battlefield[coords].hit()

    # def action_shape(self, action_name):
    #     if action_name in self.action_shapes:
    #         return self.action_shapes[action_name]
    #     return Settings.SHAPES[action_name]

    @check_action
    def battery(self, coords, rotation=0):
        return [self.battlefield[i].hit()
                for i in Settings.shape("battery", coords, rotation)]

    def can_be_deployed(self, battlefield, player, start_coords, rotation=0):
        if rotation % 2 != 0:
            return False

        for coords in self.shape.transform(start_coords, rotation):
            if not coords.belong_to(player) or battlefield[coords].is_full():
                return False
        return True

    def deploy(self, battlefield, player, coords, rotation=0):
        if not self.can_be_deployed(battlefield, player, coords, rotation):
            raise InvalidCommand('Chosen ship cannot be deployed there')

        self.battlefield, self.coords = battlefield, coords
        self.player = player
        self.shape = self.shape.rotate(rotation)

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
        self.undeploy()
        self.player.fleet.remove(self)

    def move(self, coords, rotation=0):
        old_coords = self.coords
        self.undeploy()
        if (self._can_be_moved(coords, rotation)):
            self.deploy(self.battlefield, self.player, coords, rotation)
        else:
            self.deploy(self.battlefield, self.player, old_coords)
            raise CannotDeployShip

    def _can_be_moved(self, coords, rotation=0):
        return (self._move_cost(coords, rotation) <= self.resourses['fuel'] and
                self.can_be_deployed(self.battlefield, self.player,
                                     coords, rotation))

    def _move_cost(self, coords, rotation):
        return len(self.coords - coords) + self._rotate_cost(rotation)

    def _rotate_cost(self, rotation):
        """ Ships can only be rotated by 90, 180, 270 degrees
            In ingame rotation units those are 2, 4 and 6
            2(90deg), 6(270deg) => 1; 4(180deg) => 2 """
        return (rotation / 2 % 4 - 1) % 2 + 1

    @check_action
    def radar_scan(self, coords, rotation=0):
        return [self.battlefield[i].radar_scan()
                for i in Settings.shape("radar_scan", coords, rotation)]
        # return [self.battlefield[i].radar_scan() for i in coords.in_range(3)]

    @check_action
    def air_strike(self, coords, rotation=0):
        result = {}
        for coords in Settings.shape("air_strike"):
            result[coords] = self.battlefield[coords].air_strike()
            if result[coords] == "aircraft destroyed":
                break

        # aircraft isn't lost if it wasnt destroyed unlike other resources
        if "aircraft destroyed" not in result.values():
            self.resourses['aircrafts'] += 1

        return result
        # return [self.battlefield[i].air_strike()
        #         for i in coords.in_direction(direction, 3)]

    @check_action
    def torpedo(self, coords, direction):
        result = {}
        while coords in self.battlefield:
            coords += direction
            result[coords] = self.battlefield[coords].torpedo_hit()
            if result[coords] != "miss":
                break
        return result

    @check_action
    def radar_jam(self, coords, rotation=0):
        for i in Settings.shape("radar_jam", coords, rotation):
            self.battlefield[i].deploy_anti("radar")

    @check_action
    def anti_air(self, coords, rotation=0):
        for i in Settings.shape("anti_air", coords, rotation):
            self.battlefield[i].deploy_anti("air")

    @check_action
    def torpedo_net(self, coords, rotation=0):
        for i in Settings.shape("torpedo_net", coords, rotation):
            self.battlefield[i].set_torpedo_net()
