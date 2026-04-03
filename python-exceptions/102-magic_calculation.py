#!/usr/bin/python3
def magic_calculation(a, b):
    res = 0

    for i in range(1, 3):
        try:
            if i > a:
                res = b + a
                raise Exception("Too far")

        except:
            break

        res += a ** b / i

    return res
