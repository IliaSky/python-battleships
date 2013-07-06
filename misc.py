class ShipPart:

    def __init__(self, owner):
        self.owner = owner
        self._hit = False

    def hit(self):
        if not self._hit:
            self.owner.hit()
        self._hit = True
        return "hit " + self.owner.name


class Terrain:
    pass


class TorpedoNet:
    pass
