"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?

https://www.youtube.com/watch?v=UtGtF6nc35g
"""

def largestSum(arr):
    inc = arr[0]
    exc = 0
    for i in range(1, len(arr)):
        t = inc
        inc = max(exc + arr[i], inc)
        exc = t
    return inc

print(largestSum([5, 1, 5, 5, -2, -1]))
