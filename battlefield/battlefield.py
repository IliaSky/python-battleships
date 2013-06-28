class Battlefield():

    def __init__(self, size):
        self.size = size
        width, height = 2 * size.x, 2 * size.y
        self.matrix = [[Cell() for x in range(width)] for y in range(height)]

    def __getitem__(self, key):
        key += self.size
        return self.matrix[key.y][key.x]

    def __setitem__(self, key, value):
        key += self.size
        self.matrix[key.y][key.x].contents = value
