"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def product_of_element(arr):
    n = len(arr)
    left_array = [1] * n
    right_array = [1] * n
    product_array = [None] * n

    for i in range(1, n):
        left_array[i] = arr[i-1] * left_array[i-1]

    for j in range(n-2, -1, -1):
        right_array[j] = arr[j+1] * right_array[j+1]

    for k in range(n):
        product_array[k] = left_array[k] * right_array[k]

    return product_array

input_arr = [3, 2, 1]
print(product_of_element(input_arr))
