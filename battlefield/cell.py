class Cell():

    def __init__(self, contents=None):
        if not isinstance(contents, (WorldObject, type(None))):
            raise TypeError
        self.contents = contents

    def is_empty(self):
        return self.contents is None

    def empty(self):
        self.contents = None

    def contains(self, type_):
        return isinstance(self.contents, type_)
