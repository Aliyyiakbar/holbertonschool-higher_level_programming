#!/usr/bin/python3
"""Defines a helper function for adding attributes."""


def add_attribute(obj, attr, value):
    """Add a new attribute to an object when possible.

    Args:
        obj: The object that will receive the attribute.
        attr: The name of the new attribute.
        value: The value of the new attribute.

    Raises:
        TypeError: If the object cannot receive new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, value)
