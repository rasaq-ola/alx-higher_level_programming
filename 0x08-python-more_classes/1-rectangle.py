#!/usr/bin/python3
"""Defines a real definition of a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The new width value.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The new height value.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def dict(self):
        """Return a dictionary representation of the rectangle."""
        return {'width': self.width, 'height': self.height}


if __name__ == "__main__":
    # Test cases
    try:
        myrectangle = Rectangle(2, -3)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        myrectangle = Rectangle(-2, 3)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        myrectangle = Rectangle(2, 3)
        myrectangle.width = -4
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        myrectangle = Rectangle(2, 3)
        myrectangle.width = "4"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        myrectangle = Rectangle(2, 3)
        myrectangle.height = -4
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        myrectangle = Rectangle(2, 3)
        myrectangle.height = "4"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    myrectangle = Rectangle(2, 4)
    print(sorted(myrectangle.dict()))

    myrectangle = Rectangle(2, 4)
    print(myrectangle.width)

    myrectangle = Rectangle(2, 4)
    print(myrectangle.height)

    myrectangle = Rectangle(4)
    print("{} - {}".format(myrectangle.width, myrectangle.height))

    myrectangle = Rectangle()
    print("{} - {}".format(myrectangle.width, myrectangle.height))

    myrectangle = Rectangle(2, 4)
    print("{} - {}".format(myrectangle.width, myrectangle.height))
    myrectangle.width = 10
    print("{} - {}".format(myrectangle.width, myrectangle.height))

    myrectangle = Rectangle(2, 4)
    print("{} - {}".format(myrectangle.width, myrectangle.height))
    myrectangle.height = 10
    print("{} - {}".format(myrectangle.width, myrectangle.height))

    try:
        myrectangle = Rectangle(2, "3")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        myrectangle = Rectangle("2", 3)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
