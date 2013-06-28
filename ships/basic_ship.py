class BasicShip:

    def __init__(self, player, shape, additional={}):
        """ Initiates a basic ship
            Note that the shape is always linear so it is represented
            with a vector pointing from the front to the back of the ship """

        self.player, self.shape = player, shape
        self.parts = [ShipPart(self) for i in range(len(shape))]

        for key, value in additional.items():
            self.__dict__[key] = value

    def fire_gun(self, battlefield, coords):
        battlefield[coords].hit()

    def rotate(self, angle):
        self.shape = self.shape.rotate(angle)

    def can_be_deployed(self, battlefield, start_coords, rotation=0):
        player, new_shape = self.player, self.shape.rotate(rotation)
        mock_ship = BasicShip(player, new_shape, {coords: start_coords})

        for coords in mock_ship.parts_coords():
            if not coords.belong_to(player) or battlefield[coords].is_full():
                return False
        return True

    def deploy(self, battlefield, coords, rotation=0):
        self.coords = coords
        self.rotate(rotation)
        for coords, part in zip(self.parts_coords(), self.parts):
            battlefield[coords] = part

    def parts_coords(self):
        coords, shape = self.coords, self.shape
        return [coords + i * shape.direction() for i in range(len(shape))]


class ShipPart:

    def __init__(self, owner):
        self.owner = owner
        self._hit = False

    def hit(self):
        self._hit = True
        return self.owner.name
