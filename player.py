from errors import InvalidPlayerPosition, PlayerLeft
import re


class Player:

    def __init__(self, quadrant, allies=[]):
        if quadrant not in [1, 2, 3, 4]:
            raise InvalidPlayerPosition
        self.position = quadrant
        self.allies = allies

    def add_ally(self, ally):
        self.allies.append(ally)
        ally.allies.append(self)

    def cin(self, message=""):
        player_input = input(message)
        if player_input == "exit" or player_input == "surrender":
            raise PlayerLeft(self)
        return player_input

    def cout(self, message):
        print(message)

    def choose_fleet(self, available_fleets):
        chosen = None
        while chosen not in available_fleets:
            chosen = self.cin("Choose your fleet")
        self.fleet = chosen

    def deploy_fleet(self, battlefield):
        for ship in self.fleet:
            coords = self.cin("Enter ship coordinates:")
            while not ship.can_be_deployed(battlefield, self, coords):
                self.cout("Invalid ship coords and rotation combo")
                coords = self.cin("Enter ship coordinates:")

    def make_move(self):
        self.execute_command(self.get_command(self.cin()))

    def execute_command(self):
        pass

    def get_command(self, command_string):
        m = command_string.ma
