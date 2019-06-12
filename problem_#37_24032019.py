"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.


https://www.youtube.com/watch?v=bGC2fNALbNU
https://www.geeksforgeeks.org/power-set/
"""

def all_subset(arr):
    subset = [None] * len(arr)
    helper(arr, subset, 0)

def helper(arr, subset, i):
    if i == len(arr):
        print(subset)
    else:
        subset[i] = None
        helper(arr, subset, i+1)
        subset[i] = arr[i]
        helper(arr, subset, i+1)

if __name__ == '__main__':
    all_subset([1, 2, 3])


