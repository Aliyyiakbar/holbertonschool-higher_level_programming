#!/usr/bin/python3
import dis

def magic_calculation(a, b):
    for i in range(4, 6):
        a = a + i

    return a - b


print(dis.dis(magic_calculation))

