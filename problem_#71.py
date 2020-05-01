"""
This problem was asked by Two Sigma.

Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a function rand5() that returns an integer from 1 to 5 (inclusive).
"""

from random import randint

def random():
    return randint(0, 5)

def my_rand():
    i = 0
    i = (5 * random()) + (random() - 5)
    if (i < 22):
        if i < 0:
            return (i % 7 - 7) + 1
        else:
            return (i % 7) + 1

    return my_rand()

if __name__ == '__main__':
    print(my_rand())
