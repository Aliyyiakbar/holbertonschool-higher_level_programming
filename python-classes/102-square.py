#!/usr/bin/python3
"""Define a Square class."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size (int or float): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get the square size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the square size."""
        if type(value) not in (int, float):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two squares have equal areas."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares have different areas."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if this square area is less than another."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if this square area is less than or equal to another."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if this square area is greater than another."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if this square area is greater than or equal to another."""
        return self.area() >= other.area()
