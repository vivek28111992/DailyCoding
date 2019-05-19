"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.


https://www.geeksforgeeks.org/trapping-rain-water/
https://www.youtube.com/watch?v=KV-Eq3wYjxI
"""

def findWater(arr, n):

    # left[i] contains height of tallest bar to the left of ith bar including itself
    left = [0]*n

    # Right [i] contains height of tallest bar to the right of ith bar including itself
    right = [0]*n

    # Initialize result
    water = 0

    # Fill left array
    left[0] = arr[0]
    for i in range(1, n):
        left[i] = max(left[i-1], arr[i])

    print('left array ', left)

    # Fill right array
    right[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i+1], arr[i])

    print('right arr ', right)

    # Calculate the accumulated water element by element consider the amount of water on ith bar, the amount of water accumulated on this particular bar will be equal to min(left[i], right[i]) - arr[i]
    for i in range(0, n):
        water += min(left[i], right[i]) - arr[i]

    return water

print(findWater([1, 5, 2, 3, 1, 7, 2, 4], 8))