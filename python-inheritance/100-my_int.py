#!/usr/bin/python3
"""Defines a rebel integer class."""


class MyInt(int):
    """Represent an integer with inverted equality operators."""

    def __eq__(self, other):
        """Invert the == operator."""
        return int(self) != other

    def __ne__(self, other):
        """Invert the != operator."""
        return int(self) == other
