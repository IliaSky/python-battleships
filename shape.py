from vec2d import Vec2D


class Shape:

    def __init__(self, coords_list, rotation_center=None):
        self.coords = coords_list
        self.center = rotation_center or self.coords[0]

    def __contains__(self, item):
        return self.coords.__contains__(item)

    def __iter__(self):
        for coords in self.coords:
            yield coords

    def __len__(self):
        return len(self.coords)

    def rotate(self, rotation):
        return Shape([coords.rotate(rotation, self.center)
                      for coords in self.coords], self.center)

    def translate(self, offset):
        return Shape([coords + offset for coords in self.coords],
                     self.center + offset)

    def transform(self, translation, rotation):
        return self.rotate(rotation).translate(translation)


def line(length):
    return Shape([Vec2D(i, 0) for i in range(length)])


def square(size):
    return Shape([Vec2D(i, j) for i in range(size) for j in range(size)])
