class Battlefield():

    def __init__(self, size, teams):
        """ Initializes the battlefield, where:
            + size is the size of a player's side (x, y)
              - the actual battlefield will have twice those ammounts """
        self.size = size
        size *= 2
        self.matrix = [[Cell() for x in range(size.x)] for y in range(size.y)]

    @translate_key(self.size)
    def __getitem__(self, key):
        return self.matrix[key.y][key.x]

    @translate_key(self.size)
    def __setitem__(self, key, value):
        self.matrix[key.y][key.x].contents = value

    def translate_key(offset):
        def wrap(f):
            def translated(*args):
                args.key += offset
                return f(args)
            return translated
        return wrap
