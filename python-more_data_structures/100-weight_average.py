#!/usr/bin/python3
def weight_average(my_list=[]):
    s, c = 0, 0
    for i in my_list:
        s += i[0] * i[1]
        c += i[1]

    return 0 if c == 0 else s / c
