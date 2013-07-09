from ship import Ship
from shape import square, line


class Fleets:

    BASIC_FLEET = [
        Ship("Boat", line(2), {"fuel": 0}),
        Ship("Submarine", line(3), {"fuel": 0}),
        Ship("Destroyer", line(3), {"fuel": 0}),
        Ship("Battleship", square(2), {"fuel": 0}),
        Ship("Carrier", line(5), {"fuel": 0}),
    ]

    MOBILE_FLEET = [
        Ship("Boat", line(2), {"fuel": 20}),
        Ship("Submarine", line(3), {"fuel": 20}),
        Ship("Destroyer", line(3), {"fuel": 30}),
        Ship("Battleship", square(2), {"fuel": 30}),
        Ship("Carrier", line(5), {"fuel": 30}),
    ]

    HIDDEN_FLEET = [
        Ship("Boat", line(1), {"fuel": 15}),
        Ship("Submarine", line(2), {"fuel": 15})
    ]

    NORMAL_FLEET = [
        Ship("Boat", line(2), {"torpedos": 2}),
        Ship("Submarine", line(3), {"torpedos": 3, "torpedos_nets": 8}),
        Ship("Destroyer", line(3), {"battery": -1, "scans": 4}),
        Ship("Battleship", square(2), {"anti_air": -1, "jams": -1, "battery": -1}),
        Ship("Carrier", line(5), {"aircrafts": 3})
    ]

    UNDERWATER_FLEET = [
        Ship("Boat", line(2), {"torpedos": 3}),
        Ship("Submarine 1", line(3), {"torpedos": 3, "torpedos_nets": 4}),
        Ship("Submarine 2", line(3), {"torpedos": 4, "torpedos_nets": 8}),
        Ship("Battleship", line(4), {"anti_air": -1, "radar_jam": -1, "battery": -1}),
        Ship("Carrier", line(5), {"aircrafts": 3})
    ]

    AIRFORCE_FLEET = [
        Ship("Boat", line(2), {"torpedos": 2}),
        Ship("Submarine", line(3), {"torpedos": 4, "torpedos_nets": 8}),
        Ship("Defender", line(3), {"scans": 3, "anti_air": -1, "radar_jam": -1}),
        Ship("Carrier 1", line(4), {"aircrafts": 2}),
        Ship("Carrier 2", line(4), {"aircrafts": 4})
    ]

    # UNUSUAL_FLEET = [
    #     Ship("Boat", line(2), {"torpedos": 3}),
    #     Ship("Submarine", line(3), set("torpedo_net"),
    #          {"torpedos": 4, "torpedos_nets": 8}),
    #     Ship("Defender", line(3), {"anti_air": -1, "radar_jam": -1, "scans": 3}),
    #     Ship("Carrier 1", line(4), {"aircrafts": 2}),
    #     Ship("Carrier 2", line(4), {"aircrafts": 4})
    # ]

    BATTERY_FLEET = [
        Ship("Fast Boat", line(2), {"fuel": 40}),
        Ship("Submarine", line(3), {"fuel": 5, "torpedos": 2}),
        Ship("Destroyer", square(2), {"fuel": 30, "battery": -1, "aircrafts": 1}),
        Ship("Battlestation", square(3),
             {"fuel": 15, "battery": -1, "scans": 5, "aircrafts": 3}),
    ]

    ALL = {
        "basic": BASIC_FLEET,
        "hidden": HIDDEN_FLEET,
        "mobile": MOBILE_FLEET,
        "normal": NORMAL_FLEET,
        "underwater": UNDERWATER_FLEET,
        "airforce": AIRFORCE_FLEET,
        "battery": BATTERY_FLEET
    }


for fleet in Fleets.ALL.values():
    for id, ship in enumerate(fleet):
        ship.id = id
