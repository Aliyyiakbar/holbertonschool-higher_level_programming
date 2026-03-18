#!/usr/bin/python3
def uppercase(str):
    if (len(str) == 0):
        print()
        return

    for i in range(len(str)):
        print("{}".format(chr(ord(str[i]) - (32 if ord('a') <= ord(str[i]) <= ord('z') else 0))), end=("" if i != len(str) - 1 else "\n"))
