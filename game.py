from random import shuffle


from settings import Settings
from player import Player
from battlefield import Battlefield
from errors import PlayerLeft
from ui.printer import battlefield_print


class Game:

    def __init__(self):
        player_count = self._get_player_count()
        self.players = self.init_players(player_count)
        self.battlefield = Battlefield(Settings.BATTLEFIELD_SIZE)

        self.prepare_fleets()
        # self.ask_for_alliances()
        self.start()

    def _get_player_count(cls):
        player_count = None
        while player_count not in [2, 3, 4]:
            player_count = int(input("How many players will play? (2, 3 or 4) "))
        return player_count

    def init_players(cls, player_count):
        player_positions = [i + 1 for i in range(4)]
        shuffle(player_positions)
        players = [Player(i) for i in player_positions[:player_count]]
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
                    for action in range(Settings.ACTIONS_PER_TURN):
                        move_result = player.make_move()
                        battlefield_print(self.battlefield)
                        print(str(move_result))
                except PlayerLeft as e:
                    self.players.remove(e.player)
                    if not self.is_in_progress():
                        print(str(self.alive_players()[0]) + " won!")
                        break

    def alive_players(self):
        return [player for player in self.players if player.fleet != []]

    def is_in_progress(self):
        # return len(set([player.team for player in self.alive_players()])) >= 1
        return len(self.alive_players()) != 1

    def ask_for_alliances(self):
        for player in self.players:
            if (player.cin("Will you team up? (y|n)", "(y|n)") == 'y'):
                optional_allies = [other.position for other in self.players
                                   if other != self]
                ally = player.cin("Ok. With: (1..4)", optional_allies)
                player.add_ally(ally)


if __name__ == '__main__':
    Game()
