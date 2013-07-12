class PlayerLeft(Exception):

    def __init__(self, player):
        self.player = player
        self.message = "Player {} has left".format(player.name)


class InvalidPlayerPosition(Exception):
    pass


class CannotDeployShip(Exception):
    pass


class DirectionNotSupported(Exception):
    pass


class InvalidCommand(Exception):
    pass


class InvalidCoordinates(Exception):

    def __init__(self, string):
        self.string = string
        self.message = "'{}' are not valid coordinates".format(string)

# class InsufficientAmmunition(Exception):
#     pass


class NonDeployedShipTriesToAct(Exception):
    pass


# class InvalidShipId(Exception):
#     pass


# class InvalidShipAction(Exception):
#     pass


# class ActionNotInsideBattlefield(Exception):
#     pass
