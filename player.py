import re


from errors import InvalidPlayerPosition, PlayerLeft
from settings import Settings
from fleets import Fleets
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
        self.fleet = Fleets.ALL["hidden"]
        for i, ship in enumerate(self.fleet):
            ship.id = i

    def deploy_fleet(self, battlefield):
        for ship in self.fleet:
            battlefield_print(battlefield, Vec2D(0, 0))
            coords = Vec2D.parse(self.cin("Enter ship coordinates: (x, y)",
                                          r'\(?(-?[0-9]*) ?,? ?(-?[0-9]*)\)?'))
            rotation = int(self.cin("Enter rotation (0-7)", r'-?[0-7]'))
            while not ship.can_be_deployed(battlefield, self, coords, rotation):
                self.cout("Invalid ship coords and rotation combo")
                coords = Vec2D.parse(self.cin("Enter ship coordinates: (x, y)",
                                              r'\(?(-?[0-9]*) ?,? ?(-?[0-9]*)\)?'))
                rotation = int(self.cin("Enter rotation (0-7)", r'-?[0-7]'))
            ship.deploy(battlefield, self, coords, rotation)


    # def choose_and_deploy_fleet(self, battlefield):
    #     self.choose_fleet()
    #     self.deploy_fleet(battlefield)

    def make_move(self):
        self.execute_command(self.get_command(self.cin()))

    def execute_command(self):
        pass

    def get_command(self, command_string):
        m = command_string.ma
