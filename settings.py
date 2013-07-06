from shape import Shape
from vec2d import Vec2D


class Settings:

    ACTION_RESOURSES = {"move": "fuel", "scan": "radar", "radar_jam": "jams",
                        "air_strike": "aircrafts", "anti_air": "anti_air",
                        "torpedo": "torpedos", "torpedo_net": "torpedos_nets"}

    ACTION_SHAPES = {"scan": Shape.square(3), "radar_jam": Shape.square(4),
                     "air_strike": Shape.line(3), "anti_air": Shape.square(4),
                     "torpedo_net": Shape.line(3), "fire_battery":
                     Shape([direction for direction in Vec2D.directions()
                            if direction.square_length() == 1], Vec2D(0, 0))}

    @classmethod
    def shape(cls, action_name):
        return cls.ACTION_SHAPES[action_name]

    @classmethod
    def resourse(cls, action_name):
        return cls.ACTION_RESOURSES[action_name]
