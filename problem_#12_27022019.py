"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""

# def ways_to_climb(n):
#     s1 = 1
#     s2 = 2
#
#     if s1 == n:
#         return s1
#
#     if s2 == n:
#         return s2
#
#     return ways_to_climb(n-1) + ways_to_climb(n-2)


def ways_to_X(n):
    arr = [1, 3, 5]
    if n == 1:
        return 1

    if n in arr:
        return ways_to_X(n-1) + 1

    if n > 5:
        return ways_to_X(n-5) + ways_to_X(n-3) + ways_to_X(n-1)
    elif n > 3:
        return ways_to_X(n-3) + ways_to_X(n-1)
    else:
        return ways_to_X(n-1)

if __name__ == '__main__':
    print(ways_to_X(10))
    # print(ways_to_climb(10))