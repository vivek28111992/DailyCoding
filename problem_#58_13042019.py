"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.


https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/
"""

def index_of_number(rotated_array, n):
    l = len(rotated_array)

    if l < 1:
        return 'Invalid Array'
    elif l == 1:
        if rotated_array[0] == n:
            return 0
        else:
            return None
    else:

        pivot = l // 2

        if n < rotated_array[0]:
            for i in range(pivot, l):
                if rotated_array[i] == n:
                    return i
            return None
        else:
            for i in range(pivot):
                if rotated_array[i] == n:
                    return i
            return None

if __name__ == '__main__':
    res = index_of_number([13, 18, 25, 2, 8, 10], 10)
    print(res)