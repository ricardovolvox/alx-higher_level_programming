#!/usr/bin/python3

def print_last_digit(number):
    final_digit = abs(number) % 10
    print(final_digit, end="")
    return final_digit
