class Game:

    def __init__(self, battlefield, players, available_fleets):
        self.battlefield = battlefield
        self.players = players
        self.available_fleets = available_fleets

        # if player_count in range(4):
        #     self.players = [Player(i) for i in range(player_count)]

    def start(self):
        for player in self.players:
            player.choose_fleet(self.available_fleets)
            player.deploy_fleet(self.battlefield)

        while self.is_in_progress():
            for player in self.alive_players():
                player.make_move()

    def alive_players(self):
        return [player for player in self.players if player.ships != []]

    def is_in_progress(self):
        return len(set([player.team for player in self.alive_players()])) == 1
