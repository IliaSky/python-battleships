class Cell():

    def __init__(self, contents=None):
        self.contents = contents
        self.defence = {"air": False, "radar": False, "torpedo": False}

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

    def hit(self):
        if self.check_for_ship():
            return self.contents.hit()
        return "miss"

    def deploy_anti(self, key):
        self.defence[key] = True

    def radar_scan(self):
        if self.defence[radar]:
            return "jammed"
        return ["empty", "ship"][self.check_for_ship()]

    def air_strike(self):
        if self.defence[air]:
            return "aircraft destroyed"
        return self.hit()

    def torpedo_hit(self):
        if self.check_for_ship():
            return self.hit()
