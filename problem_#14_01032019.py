"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.

https://www.geeksforgeeks.org/estimating-value-pi-using-monte-carlo/
"""

import random

def pi(interval):
    circle_points = 0
    square_points = 0
    i = 0
    while i < (interval*interval):
        x = float(random.randint(0, interval) % (interval+1)) / interval
        y = float(random.randint(0, interval) % (interval+1)) / interval

        d = x*x + y*y

        if d <= 1:
            circle_points += 1

        square_points += 1
        est_pi = float(4 * circle_points) / square_points

        i += 1

    return est_pi

if __name__ == '__main__':
    print(pi(100))


