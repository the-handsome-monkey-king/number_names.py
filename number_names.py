#!/usr/bin/env python
"""number_names.py

Spell out a number name, up to one million, in English."""

__author__ = "Ryan Morehouse"
__license__ = "MIT"

import sys

below_twenty = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"}

tens = {
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"}

def get_name(n):
    if n < 20:
        return below_twenty[n]
    elif n < 100:
        r = n % 10
        if r == 0:
            return tens[n]
        else:
            t = n - r
            return "{} {}".format(tens[t], below_twenty[r])
    elif n < 1000:
        r = n % 100
        h = n / 100
        if r == 0:
            return "{} hundred".format(below_twenty[h])
        else:
            s1 = "{} hundred".format(below_twenty[h])
            s2 = get_name(r)
            return "{} {}".format(s1, s2)
    elif n < 10000:
        r = n % 1000
        thou = n / 1000
        if r == 0:
            return "{} thousand".format(below_twenty[thou])
        else:
            s1 = "{} thousand".format(below_twenty[thou])
            s2 = get_name(r)
            return "{} {}".format(s1, s2)
    else:
        return "Above 1 million, out of range."
        
def main():
    try:
        n = (int)(sys.argv[1])
        if n < 0:
            raise ValueError
    except(ValueError, IndexError):
        print("Usage: number_names.py [n]")
        print("[n] = a postive integer up to one million")
        sys.exit(1)

    print(get_name(n))

if __name__ == "__main__":
    main()
