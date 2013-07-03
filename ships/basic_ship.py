from misc import ShipPart


class BasicShip:

    def __init__(self, player, shape, additional={}):
        self.player, self.shape, self.hp = player, shape, len(shape)
        self.parts = [ShipPart(self) for i in range(len(self))]

        for key, value in additional.items():
            self.__dict__[key] = value

    def __len__(self):
        return len(self.shape)

    def fire_gun(self, battlefield, coords):
        battlefield[coords].hit()

    def rotate(self, rotation):
        """ Ships can only be rotated by a value of k * pi / 4
            In ingame units that means that the unit value must be even """
        if rotation % 2 == 0:
            self.shape = self.shape.rotate(rotation)

    def can_be_deployed(self, battlefield, start_coords, rotation=0):
        if rotation % 2 != 0:
            return False

        for coords in self.shape.translate(start_coords).rotate(rotation):
            if not coords.belong_to(self.player) or battlefield[coords].is_full():
                return False
        return True

    def deploy(self, battlefield, coords, rotation=0):
        self.coords = coords
        self.rotate(rotation)
        for coords, part in zip(self.parts_coords(), self.parts):
            battlefield[coords] = part

    def undeploy(self, battlefield):
        for coords, part in zip(self.parts_coords(), self.parts):
            battlefield[coords] = None

    def parts_coords(self):
        return self.shape.translate(self.coords)

    def hit(self):
        self.hp -= 1
