#!/usr/bin/python3
import builtins


def main():
    a = dir("hidden_4.pyc")
    b = []

    for i in sorted(a):
        if i[0] == '_':
            continue
        b.append(i)

    print(*b, sep='\n')


if __name__ == "__main__":
    main()
