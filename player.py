from errors import InvalidPlayerPosition


class Player:

    def __init__(self, quadrant, allies=[]):
        if quadrant not in [1, 2, 3, 4]:
            raise InvalidPlayerPosition
        self.position = quadrant
        self.allies = allies

    def add_ally(self, ally):
        self.allies.append(ally)
        ally.allies.append(self)
