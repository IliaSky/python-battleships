class Ship:

    def __init__(self, player, shape):
        self.player, self.shape = player, shape


class ShipPart:

    def __init__(self, owner):
        self.owner = owner
        self._hit = False

    def hit(self):
        self._hit = True
        return self.owner.name


class ShipBow(ShipPart):
    pass
