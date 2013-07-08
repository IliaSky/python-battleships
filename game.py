from random import shuffle
from settings import Settings
from player import Player
from battlefield import Battlefield
from errors import PlayerLeft
import time
import traceback


class Game:

    def __init__(self):
        try:
            player_count = self._get_player_count()
            self.players = self.init_players(player_count)
            self.battlefield = Battlefield(Settings.BATTLEFIELD_SIZE)

            self.prepare_fleets()
            self.ask_for_alliances()
        except Exception as e:
            traceback.print_exc()
        finally:
            time.sleep(1000)
        # if player_count in range(4):
        #     self.players = [Player(i) for i in range(player_count)]

    def _get_player_count(cls):
        player_count = None
        while player_count not in [2, 3, 4]:
            player_count = input("How many players will play? (2, 3 or 4) ")
        return player_count

    def init_players(cls, player_count):
        player_positions = [i + 1 for i in range(player_count)]
        shuffle(player_positions)
        players = [Player(i) for i in player_positions]
        print("You will be " + str(players))
        return players

    def prepare_fleets(self):
        for player in self.players:
            player.choose_fleet()
            player.deploy_fleet(self.battlefield)

    def start(self):
        while self.is_in_progress():
            for player in self.alive_players():
                try:
                    player.make_move()
                except PlayerLeft as e:
                    self.players.remove(e.player)

    def alive_players(self):
        return [player for player in self.players if player.fleet != []]

    def is_in_progress(self):
        return len(set([player.team for player in self.alive_players()])) == 1

    def ask_for_alliances(self):
        for player in self.players:
            if (player.cin("Will you team up? (y|n)", "(y|n)") == 'y'):
                optional_allies = [other.quadrant for other in self.players
                                   if other != self]
                ally = player.cin("Ok. With: (1..4)", optional_allies)
                player.add_ally(ally)


# def matches(regex):
#     def matcher(f):
#         def decorated(*args):
#             for (i, (arg, t)) in enumerate(zip(args, types)):
#                 if not isinstance(arg, t):
#                     raise TypeError("Argument #{0} of '{1}' should \
#                        have been of type {2}".format(i,
#                                            f.__name__,
#                                            t.__name__))
#                   #TODO: more complex checks
#                 return f(*args)
#             return decorated
#     return matcher

# def match(regex):
#     return
from vec2d import Vec2D
import re
print(type(Battlefield(Settings.BATTLEFIELD_SIZE)))
a = re.match(r"<class '(?:.*)\.(.*)'>", str(type(Vec2D(3, 3)))).groups()[0]
print(a)
print(a)
print(a)
# if __name__ == '__main__':
#     Game()
