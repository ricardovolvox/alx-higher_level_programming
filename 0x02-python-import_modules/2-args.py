#!/usr/bin/python3
import sys

if __name__ == "__main__":
    """Prints list of arguments"""

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print(f"{count} arguments:")
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))

