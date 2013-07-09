class ShipPart:

    def __init__(self, owner):
        self.owner = owner
        self.is_hit = False

    def hit(self):
        if not self.is_hit:
            self.owner.hit()
        self.is_hit = True
        return "hit " + self.owner.name


class Terrain:
    pass


class TorpedoNet:
    pass
