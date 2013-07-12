from shape import square, line


class Fleets:

    BASIC_FLEET = [
        ("PT Boat", line(2), {"fuel": 0}),
        ("Submarine", line(3), {"fuel": 0}),
        ("Destroyer", line(3), {"fuel": 0}),
        ("Battleship", square(2), {"fuel": 0}),
        ("Carrier", line(5), {"fuel": 0}),
    ]

    MOBILE_FLEET = [
        ("PT Boat", line(2), {"fuel": 20}),
        ("Submarine", line(3), {"fuel": 20}),
        ("Destroyer", line(3), {"fuel": 30}),
        ("Battleship", square(2), {"fuel": 30}),
        ("Carrier", line(5), {"fuel": 30}),
    ]

    HIDDEN_FLEET = [
        ("PT Boat", line(1), {"fuel": 15}),
        ("Submarine", line(2), {"fuel": 15})
    ]

    SPECIAL_FLEET = [
        ("PT Boat", line(3), {"fuel": 15, "scans": 1, "jams": -1,
                              "battery_shots": -1, "anti_air": -1,
                              "torpedos": 1, "aircrafts": 1,
                              "torpedos_nets": 1})
    ]

    NORMAL_FLEET = [
        ("PT Boat", line(2), {"torpedos": 2}),
        ("Submarine", line(3), {"torpedos": 3, "torpedos_nets": 8}),
        ("Destroyer", line(3), {"battery_shots": -1, "scans": 4}),
        ("Battleship", square(2), {"anti_air": -1, "jams": -1,
                                   "battery_shots": -1}),
        ("Carrier", line(5), {"aircrafts": 2})
    ]

    UNDERWATER_FLEET = [
        ("PT Boat", line(2), {"torpedos": 3}),
        ("Submarine", line(3), {"torpedos": 3, "torpedos_nets": 4}),
        ("Uber Submarine", line(4), {"torpedos": 4, "torpedos_nets": 8}),
        ("Battleship", line(4), {"anti_air": -1, "radar_jam": -1,
                                 "battery_shots": -1}),
        ("Carrier", line(5), {"aircrafts": 2})
    ]

    AIRFORCE_FLEET = [
        ("PT Boat", line(2), {"torpedos": 2}),
        ("Submarine", line(3), {"torpedos": 4, "torpedos_nets": 8}),
        ("Defender", line(3), {"scans": 3, "anti_air": -1, "radar_jam": -1}),
        ("Carrier", line(4), {"aircrafts": 2}),
        ("War Carrier", line(5), {"aircrafts": 3})
    ]

    BATTERY_FLEET = [
        ("PT Boat", line(2), {"fuel": 40}),
        ("Submarine", line(3), {"fuel": 5, "torpedos": 2}),
        ("Destroyer", square(2), {"battery_shots": -1, "aircrafts": 1}),
        ("Battlestation", square(3), {"fuel": 15, "battery_shots": -1,
                                      "scans": 5, "aircrafts": 3}),
    ]

    ALL = {
        "basic": BASIC_FLEET,
        "hidden": HIDDEN_FLEET,
        "spec": SPECIAL_FLEET,
        "mobile": MOBILE_FLEET,
        "normal": NORMAL_FLEET,
        "underwater": UNDERWATER_FLEET,
        "airforce": AIRFORCE_FLEET,
        "battery": BATTERY_FLEET
    }
