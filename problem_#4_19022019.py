"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

"""
O(N) solution:
Algorithm:
1) Segregate positive and negative numbers i.e. move all negative numbers to left side.
2) Now we can ignore negative elements and consider only the part of array which contains all positive elements. We traverse the array containing all positive numbers and to mark presence of an element x, we change the sign of value at index x to negative. We traverse the array again and print the first index which has positive value. During traversing, we can ignore the index value if it is greater than array size. We are bothered only for array values in range of array size.
"""


# put all 0 and negative numbers on left side of array and return count of such numbers
def segregate(arr, length):
    j = 0
    for i in range(length):
        if arr[i] < 1:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return j


# Find the smallest positive missing number in an array
def findPositive(arr, n):
    # Mark arr[i] as visited by making arr[arr[i] - 1] negative
    # Note that 1 is subtracted because index start from 0 and positive numbers start from 1
    for i in range(n):
        x = abs(arr[i])
        if x - 1 < n and arr[x - 1] > 0:
            arr[x - 1] = -arr[x - 1]
            
    # Return the first index value at which is positive
    for j in range(n):
        if arr[j] > 0:
            return j+1

    return n+1


# Find the smallest positive missing number
def findMissing(arr, length):
    # first separate positive and negative numbers
    neg = segregate(arr, length)
    return findPositive(arr[neg:], length-neg)

print(findMissing([3, 2, -1, 1], 4))
