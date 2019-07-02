"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.


https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/
"""

def binary_search(arr, start, end, key):

    if end < start:
        return -1

    mid = int((start+end)/2)

    if arr[mid] == key:
        return mid

    if key < arr[mid]:
        end = mid-1
        return binary_search(arr, start, end, key)
    else:
        start = mid+1
        return binary_search(arr, start, end, key)


def findPivot(arr, low, high):
    # base cases
    if high < low:
        return -1

    if high == low:
        return low

    mid = int((low + high) / 2)

    if arr[mid] > arr[mid+1]:
        return (mid+1)

    if arr[low] <= arr[mid]:
        return findPivot(arr, mid+1, high)
    return findPivot(arr, low, mid-1)



def index_of_number(rotated_array, key):
    l = len(rotated_array)

    if l < 1:
        return 'Invalid Array'
    else:

        pivot = findPivot(rotated_array, 0, l)
        print('pivot ', pivot)

        # If we didn't find a pivot, then array is not at all rotated
        if pivot == -1:
            return binary_search(rotated_array, 0, l-1, key)

        if rotated_array[pivot] == key:
            return pivot

        if rotated_array[pivot] < key and key < rotated_array[l-1]:
            return binary_search(rotated_array, pivot+1, l-1, key)
        return binary_search(rotated_array, 0, pivot-1, key)

if __name__ == '__main__':
    res = index_of_number([73, 85, 94, 21, 34, 47, 54, 66], 85)
    print(res)