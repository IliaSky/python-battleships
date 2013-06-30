class Cell():

    def __init__(self, contents=None, anti_air=False, anti_radar=False):
        self.contents = contents
        self.anti_air, self.anti_radar = anti_air, anti_radar

    def is_empty(self):
        return self.contents is None

    def is_full(self):
        return not self.is_empty

    def empty(self):
        self.contents = None

    def contains(self, type_):
        return isinstance(self.contents, type_)

    def check_for_ship(self):
        return self.contains(ShipPart)

    def radar_scan(self):
        if not self.anti_radar:
            return self.check_for_ship()
        raise RadarJammed

    def radar_jam(self):
        self.anti_radar = True

    def hit(self):
        """ returns the name of the ship or false if there is no ship """
        if self.check_for_ship():
            return self.contents.hit()
        return False
