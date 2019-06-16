"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.


https://www.geeksforgeeks.org/find-the-element-that-appears-once/
https://www.gohired.in/2015/01/27/find-the-element-that-appears-once-others-appears-thrice/
"""

def getSingle(arr, n):
    ones = 0
    twos = 0

    for i in range(n):
        # one & arr[i] gives the bits that are there in both 'ones' and new element from arr[]. We add these bits to 'twos' using bitwise OR
        twos = twos | (ones & arr[i])

        # one & arr[i]" gives the bits that are there in both 'ones' and new element from arr[]. We add these bits to 'twos' using bitwise OR
        ones = ones ^ arr[i]

        # The common bits are those bits which appear third time. So these bits should not be there in both 'ones' and 'twos'. common_bit_mask contains all these bits as 0, so that the bits can be removed from 'ones' and 'twos'
        not_thrice = ~(ones & twos)

        # Remove common bits (the bits that appear third time) from 'ones'
        ones = ones & not_thrice

        # Remove common bits (the bits that appear third time) from 'twos'
        twos = twos & not_thrice

    return ones

arr = [6, 1, 3, 3, 3, 6, 6]
n = len(arr)
print("The element with single occurrence is ", getSingle(arr, n))

