#!/usr/bin/python3
for character in range(97, 122 + 1):
    if chr(character) !='q' and chr(character) !='e':
        print('{}'.format(chr(character)), end='')
