class Shape:

    def __init__(self, coords_list, center=None):
        self.coords = coords_list
        self.center = rotation_center or self.coords[0]

    def __contains__(self, item):
        return self.coords.__contains__(item)

    def __len__(self):
        return len(self.coords)

    def rotate(self, rotation):
        return Shape([coords.rotate(rotation, self.center)
                      for coords in self.coords], self.center)

    def translate(self, offset):
        return Shape([coords + offset for coords in self.coords],
                     self.center + offset)

    @classmethod
    def line(cls, length):
        return cls([Vec2D(0, i) for i in range(length)])

    @classmethod
    def square(cls, size):
        return cls([Vec2D(i, j) for i in range(size) for j in range(size)])
