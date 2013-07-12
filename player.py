import re
import traceback


from errors import *
from settings import Settings
from fleets import Fleets
from ship import Ship
from vec2d import Vec2D
from ui.printer import battlefield_print


class Player:

    def __init__(self, quadrant, allies=set()):
        if quadrant not in [1, 2, 3, 4]:
            raise InvalidPlayerPosition
        self.position = quadrant
        self.name = Settings.QUADRANT_NAMES[quadrant]
        self.team = allies.union([self])

    def add_ally(self, ally):
        self.team.add(ally)
        ally.team.add(self)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def cin(self, message="", condition=r'.*'):
        """ Returns the first player input that matches the current condition
            the condition can either be a regular expression or
            an iterable containing all valid inputs. """
        valid = False
        while not valid:
            player_input = input(self.name + ": " + message)
            if player_input == "exit" or player_input == "surrender":
                raise PlayerLeft(self)
            if type(condition) is str:
                valid = re.match(condition, player_input, re.I) is not None
            else:
                valid = player_input in condition
        return player_input

    def cout(self, message):
        print(message)

    def choose_fleet(self):
        # self.cout("Choose your fleet. Your options are: {}".format(Fleets.ALL.keys()))
        # self.fleet = Fleets.ALL[self.cin("Choose your fleet: ", Fleets.ALL.keys())]
        self.fleet = [Ship(*args) for args in Fleets.ALL["spec"]]
        for ship in self.fleet:
            ship.id = Settings.SHIP_NAME_ABBR[ship.name]

    def deploy_fleet(self, battlefield):
        for ship in self.fleet:
            battlefield_print(battlefield, Vec2D(0, 0))
            coords, rotation = self.get_coords_and_rotation()
            while not ship.can_be_deployed(battlefield, self, coords, rotation):
                self.cout("Invalid ship coords and rotation combo")
                coords, rotation = self.get_coords_and_rotation()
            ship.deploy(battlefield, self, coords, rotation)
        battlefield_print(battlefield, Vec2D(0, 0))

    def get_coords_and_rotation(self):
        examples = ['', 'x y r ', '-x y r ', '-x -y r ', 'x -y r ']
        message = "Ship coordinates and rotation (optional): "
        format = r'(-?[0-9]+) (-?[0-9]+)(?: (-?[0-9]+))?'
        player_input = self.cin(message + examples[self.position], format)
        m = re.match(format, player_input)
        coords = Vec2D(int(m.groups()[0]), int(m.groups()[1]))
        rotation = int(m.groups()[2] or 0)
        return (coords, rotation)

    # def choose_ship(self):
    #     return self.cin('Choose your ship ', [ship.id for ship in self.fleet])

    def make_move(self):
        while True:
            try:
                command = self.parse_command(self.cin("Enter command: "))
                return self.execute_command(*command)
            except InvalidCommand as e:
                print(e)
                # traceback.print_exc()

    def execute_command(self, ship, action, target):
        if action == 'fire_gun':
            ship.__getattribute__(action)(target)
        else:
            ship.__getattribute__(action)(*target)

    def parse_command(self, command):
        # regex = r'([0-9]+) ([_a-z]+) \(?(-?[0-9]+,? -?[0-9]+)\)?(?: (.*))?'
        regex = r'([A-Z]) ([_a-z]+) (-?[0-9] -?[0-9])(?: (.*))?'
        try:
            m = re.match(regex, command).groups()
        except AttributeError as e:
            raise InvalidCommand('Invalid command format')

        ship_id, action, coords = m[0], m[1], Vec2D.parse(m[2])
        ships = [ship for ship in self.fleet if ship.id == ship_id]

        if len(ships) != 1:
            raise InvalidCommand('You don\'t own a ship with that name')

        if action not in Settings.RESOURSES.keys():
            raise InvalidCommand('There is no such action')

        if action == 'fire_gun':
            target = coords
        elif action == 'torpedo':
            target = (coords, Vec2D.parse(m[3]))
        else:
            target = (coords, int(m[3] or 0))

        return (ships[0], action, target)

# print(Player(3).parse_command("1 sdasda_dasdas 0 3 0 3"))
