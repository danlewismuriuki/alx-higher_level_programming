#!/usr/bin/python3

from .rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter method that returns size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter method that returns size """
        self.width = value
        self.height = value

    def __str__(self):
        """ Representation of reader friendly string of a class obj """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        if args:
            self.id = args[0] if len(args) >= 1 else self.id
            self.size = args[1] if len(args) >= 2 else self.size
            self.x = args[2] if len(args) >= 3 else self.x
            self.y = args[3] if len(args) >= 4 else self.y

        elif kwargs:
            self.id = kwargs.get("id", self.id)
            self.size = kwargs.get("size", self.size)
            self.x = kwargs.get("x", self.x)
            self.y = kwargs.get("y", self.y)

    def to_dictionary(self):
        myDict = dict(id = self.id, size = self.size, x = self.x, y = self.y)
        return myDict
