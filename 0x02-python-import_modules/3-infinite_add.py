#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arguments = argv[1:]
    if not arguments:
        print("0")
    else:
        result = sum(map(int, arguments))
        print(str(result))
