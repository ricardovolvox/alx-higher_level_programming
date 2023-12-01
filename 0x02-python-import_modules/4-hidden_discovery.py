#!/usr/bin/python3
import sys
import hidden_4 as secret

if __name__ != "__main__":
    exit()

for title in dir(secret):
    if title[0:2] != "__":
        print(title)
