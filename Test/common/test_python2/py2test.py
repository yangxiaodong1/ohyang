# coding: utf-8
from sys import argv


def print_log(name1, name2, name3):
    print(name1 + name2 + name3)
    return "world"


if __name__ == "__main__":
    print_log(argv[1], argv[2], argv[3])
