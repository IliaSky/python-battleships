class Player:

    def __init__(self, battlefield_position, allies=[]):
        if battlefield_position not in range(4):
            raise InvalidPositionError
        self.position = battlefield_position
        self.allies = allies

    def add_ally(self, ally):
        allies.append(ally)
        ally.allies.append(self)
