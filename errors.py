class InvalidPlayerPosition(Exception):
    pass


class CannotDeployShip(Exception):
    pass


class DirectionNotSupported(Exception):
    pass


class InvalidShipAction(Exception):
    pass


class InsufficientAmmunition(Exception):
    pass


class NonDeployedShipTriesToAct(Exception):
    pass


class PlayerLeft(Exception):

    def __init__(self, player):
        self.player = player
        self.message = "Player {} has left".format(player.name)


class InvalidCoordinatesString(Exception):

    def __init__(self, string):
        self.string = string
        self.message = "'{}' are not valid coordinates".format(string)


def InvalidAction(self):
    pass
