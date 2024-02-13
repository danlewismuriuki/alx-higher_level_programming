#!/usr/bin/python3
# rectangle.py

# Base = __import__("base").Base
from .base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter for the width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for the width attribute """
        self.validate_integer("width", value)
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for the height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for ther height atttribute """
        self.validate_integer("height", value)
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter for the width attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for ther x atttribute """
        self.validate_integer("x", value)
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter for the y attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for the x atttribute """
        self.validate_integer("y", value)
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def validate_integer(self, name, value):
        """ Validates if the value is an integer """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

    def area(self):
        return (self.__height * self.__width)

    def display(self):
        """ Prints the Rectangle instance with '#' characters """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        return "[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".format(
                self.id, self.__x, self.__y, self.__width, self.__height
                )

    # def update(self, *args):
    #    attributes = ["id", "width", "height", "x", "y"]
    #    for i in range(min(len(args), len(attributes))):
    #       setattr(self, attributes[i], args[i])

    def update(self, *args, **kwargs):
        if args:
            self.id = arg[0] if len(args) >= 1 else self.id
            self.width = arg[1] if len(args) >= 2 else self.width
            self.height = arg[2] if len(args) >= 2 else self.height

        elif kwargs:
            self.id = kwargs.get("id", self.id)
            self.width = kwargs.get("width", self.width)
            self.height = kwargs.get("height", self.height)

    def to_dictionary(self):
        """
        myDict = {
                id: "self.id",
                width: "self.width",
                height: "self.height",
                x: "self.x",
                y: "self.y"
                }
         """
        myDict = dict(
                x=self.x,
                y=self.y,
                id=self.id,
                height=self.height,
                width=self.width
        )
        return myDict
