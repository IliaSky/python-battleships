class Ship:

    def __init__(self, player, shape, additional={}):
        """ Initiates a basic ship
            Note that the shape is always linear so it is represented
            with a vector pointing from the front to the back of the ship """

        self.player, self.shape = player, shape
        for key, value in additional.items():
            self.__dict__[key] = value

    def rotate(self, angle):
        self.shape.rotate(angle)


class ShipPart:

    def __init__(self, owner):
        self.owner = owner
        self._hit = False

    def hit(self):
        self._hit = True
        return self.owner.name


class ShipBow(ShipPart):
    pass
