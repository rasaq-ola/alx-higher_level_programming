#!/usr/bin/python3
"""Define a Rectangle class."""


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

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


if __name__ == "__main__":
    # Test cases
    myrectangle = Rectangle(2, 4)
    print("{} - {} => {}".format(myrectangle.width, myrectangle.height, myrectangle.area()))

    myrectangle = Rectangle(2, 4)
    print("{} - {} => {}".format(myrectangle.width, myrectangle.height, myrectangle.perimeter()))

    myrectangle = Rectangle(10, 10)
    print("{} - {} => {} / {}".format(myrectangle.width, myrectangle.height, myrectangle.area(), myrectangle.perimeter()))

    myrectangle = Rectangle(10)
    print("{} - {} => {} / {}".format(myrectangle.width, myrectangle.height, myrectangle.area(), myrectangle.perimeter()))

    myrectangle = Rectangle()
    print("{} - {} => {} / {}".format(myrectangle.width, myrectangle.height, myrectangle.area(), myrectangle.perimeter()))
