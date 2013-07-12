from shape import Shape, square, line
from vec2d import Vec2D


class Settings:

    RESOURSES = {"move": "fuel", "radar_scan": "scans", "radar_jam": "jams",
                 "air_strike": "aircrafts", "anti_air": "anti_air",
                 "torpedo": "torpedos", "torpedo_net": "torpedos_nets",
                 "battery": "battery_shots", "fire_gun": "gun_shots"}

    SHAPES = {"radar_scan": square(3), "radar_jam": square(4),
              "air_strike": line(3), "anti_air": square(4),
              "torpedo_net": line(3), "battery":
              Shape([direction for direction in Vec2D.directions()
                     if direction.square_length() == 1], Vec2D(0, 0))}

    BATTLEFIELD_SIZE = Vec2D(8, 8)

    QUADRANT_NAMES = ["(0) Border", "(1) Empire", "(2) Rebellion",
                      "(3) Republic", "(4) Pirates"]

    ACTIONS_PER_TURN = 2

    SHIP_NAME_ABBR = {
        "PT Boat": "P",
        "Submarine": "S",
        "Uber Submarine": "U",
        "Destroyer": "D",
        "Battleship": "B",
        "Battlestation": "T",
        "Carrier": "C",
        "War Carrier": "W",
        "Defender": "F"
    }

    @classmethod
    def shape(cls, action_name, translation=Vec2D(0, 0), rotation=0):
        return cls.SHAPES[action_name].transform(translation, rotation)

    @classmethod
    def resourse(cls, resourse_name):
        return cls.RESOURSES[resourse_name]

    COLOURS = []

#     @classmethod
#     def ship(cls, ship_name):
#         return [ship for ship in cls.NORMAL_SHIPS if ship.name == ship_name][0]


# def _easy_ship(name, length, resourses={"fuel": 10}):
#     pass
