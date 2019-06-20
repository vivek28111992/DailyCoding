"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Two Sigma.

Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function rand7() that returns an integer from 1 to 7 (inclusive).


https://stackoverflow.com/questions/137783/expand-a-random-range-from-1-5-to-1-7
"""

import random

def rand7():
    i = 25
    while i > 21:
        i = 5 * (random.randrange(1, 5) - 1) + random.randrange(1, 5)

    return i % 7 + 1

print(rand7())
