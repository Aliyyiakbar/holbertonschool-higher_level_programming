#!/usr/bin/python3
"""Defines a function that inserts text after matching lines."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a specific string.

    Args:
        filename (str): The name of the file to update.
        search_string (str): The string to search for.
        new_string (str): The string to insert after matching lines.
    """
    text = ""

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
