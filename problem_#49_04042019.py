"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.


https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
"""

def maxSum(arr):
    max_so_far = 0
    max_ending_here = 0

    for i in range(len(arr)):
        max_ending_here = max_ending_here + arr[i]

        if max_ending_here < 0:
            max_ending_here = 0

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return max_so_far

if __name__ == '__main__':
    print(maxSum([34, -50, 42, 14, -5, 86]))
