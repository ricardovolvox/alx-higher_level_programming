#!/usr/bin/python3

def uppercase(str):
    for i in str:
        if 97 <= ord(i) <= 122:
            c = chr(ord(i) - 32)
        else:
            c = i
        print("{}".format(c), end="")
    print()
