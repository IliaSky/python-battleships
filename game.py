from errors import PlayerLeft


class Game:

    def __init__(self, battlefield, players, available_fleets):
        self.battlefield = battlefield
        self.players = players
        self.available_fleets = available_fleets

        # if player_count in range(4):
        #     self.players = [Player(i) for i in range(player_count)]

    def prepare_fleets(self):
        for player in self.players:
            try:
                player.choose_fleet(self.available_fleets)
                player.deploy_fleet(self.battlefield)
            except PlayerLeft as e:
                pass

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
