class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)
        # so if the direction that we want to go is not in the room's description, that means we cannot go to that specified direction, thus the code will return None value.

    def add_paths(self, paths):
        self.paths.update(paths)
