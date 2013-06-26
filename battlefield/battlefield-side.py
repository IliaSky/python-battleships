class BattlefieldSide():

    def __init__(self, size):
        self.size = size
        self.matrix = [[Cell() for y in range(size)] for x in range(size)]

    def __len__(self):
        return self.size

    def __getitem__(self, key):
        if isinstance(key, Vec2D):
            return self.matrix[key.x][key.y]
        else:
            return self.matrix[key]
