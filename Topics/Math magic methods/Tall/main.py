class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __iadd__(self, c):
        self.height += c
        return self

    def __isub__(self, c):
        self.height -= c
        return self
