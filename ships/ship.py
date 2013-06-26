class Ship:

    def __init__(self, world, bow_coords, length, direction):
        self.world, self.length, self.direction = world, length, direction
        self.fuel = 0

        self.coords = [bow_coords - direction * i for i in range(length)]
        for coords in self.coords:
            self.world[bow_coords].contents = ShipPart(self)

        self.world[bow_coords].contents = ShipBow(self)


class WorldObject:
    pass


class ShipPart(WorldObject):

    def __init__(self, owner):
        self.owner = owner


class ShipBow(ShipPart):
    pass
