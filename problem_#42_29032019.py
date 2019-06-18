"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24


https://www.geeksforgeeks.org/subset-sum-problem-dp-25/
https://en.wikipedia.org/wiki/NP-completeness
"""

def isSubSet(set, n, sum):

    # Base Cases
    if (sum == 0):
        return True

    if (n == 0 and sum != 0):
        return False

    # If last element is greater than sum, then ignore it
    if (set[n - 1] > sum):
        return isSubSet(set, n - 1, sum)

    # else, check if sum can be obtained by any of the following
    # (a) including the last element
    # (b) excluding the last element
    return isSubSet(set, n - 1, sum) or isSubSet(set, n - 1, sum-set[n-1])

set = [3, 34, 4, 12, 5, 2]
sum = 9
n = len(set)
if (isSubSet(set, n, sum) == True) :
    print("Found a subset with given sum")
else :
    print("No subset with given sum")
