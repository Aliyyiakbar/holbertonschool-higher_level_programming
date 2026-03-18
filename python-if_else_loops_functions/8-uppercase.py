#!/usr/bin/python3
def uppercase(str):
    res = ""
    for c in str:
        res += chr(ord(c) - (32 if ord('a') <= ord(c) <= ord('z') else 0))
    return res
