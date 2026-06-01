#!/usr/bin/python3
"""
This module contains a single class, LockedClass.
It is designed to demonstrate low memory cost by preventing
the dynamic creation of instance attributes.
"""


class LockedClass:
    """
    Prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called 'first_name'.
    """
    __slots__ = ["first_name"]
