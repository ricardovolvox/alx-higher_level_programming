#!/usr/bin/python3

def remove_char_at(text, n):
    if n < 0:
        return text
    return text[:n] + text[n + 1:]
print(remove_char_at("Best School", 3))
