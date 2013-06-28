class Player:

    def __init__(self, battlefield_position):
        if battlefield_position not in range(4):
            raise InvalidPositionError
        self.position = battlefield_position
