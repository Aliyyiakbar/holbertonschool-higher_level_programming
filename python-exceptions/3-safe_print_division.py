#!/usr/bin/python3
def safe_print_division(a, b):
    res = None
    try:
        res = a / b

    except Exception as e:
        pass

    finally:
        print("{:d}".format(res))

    return res
