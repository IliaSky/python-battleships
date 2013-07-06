from misc import ShipPart
from errors import NonDeployedShipTriesToAct, CannotDeployShip


class BasicShip:

    def __init__(self, name, player, shape, additional={}):
        self.name, self.player, self.shape = name, player, shape
        self.hp = len(shape)
        self.parts = [ShipPart(self) for i in range(len(self))]

        for key, value in additional.items():
            self.__dict__[key] = value

    def __len__(self):
        return len(self.shape)

    def fire_gun(self, coords):
        if not hasattr(self, 'battlefield'):
            raise NonDeployedShipTriesToAct
        return self.battlefield[coords].hit()

    def can_be_deployed(self, battlefield, start_coords, rotation=0):
        if rotation % 2 != 0:
            return False

        for coords in self.shape.translate(start_coords).rotate(rotation):
            if not coords.belong_to(self.player) or battlefield[coords].is_full():
                return False

        return True

    def deploy(self, battlefield, coords, rotation=0):
        if not self.can_be_deployed(battlefield, coords, rotation):
            raise CannotDeployShip

        self.battlefield, self.coords = battlefield, coords
        self.shape.rotate(rotation)

        for coords, part in zip(self.parts_coords(), self.parts):
            battlefield[coords] = part

    def undeploy(self):
        for coords, part in zip(self.parts_coords(), self.parts):
            self.battlefield[coords] = None

    def parts_coords(self):
        return self.shape.translate(self.coords)

    def hit(self):
        self.hp -= 1
        if self.hp <= 0:
            self.destroy()

    def destroy(self):
        pass
