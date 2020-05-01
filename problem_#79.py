"""
This problem was asked by Facebook.

Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.
"""

def nonDecreasing(arr):
    modify = 0

    n = len(arr)

    # check for last element
    if arr[n-1] <= arr[n-2]:
        arr[n-1] = arr[n-2] - 1
        modify += 1

    # check for first element
    if arr[0] >= arr[1]:
        arr[0] = arr[1] - 1
        modify += 1

    for i in range(1, n-1):
        if (arr[i] <= arr[i-1] and arr[i] <= arr[i+1]) or (arr[i] >= arr[i-1] and arr[i] >= arr[i+1]):
            arr[i] = (arr[i-1] + arr[i+1]) // 2
            modify += 1

            if (arr[i] == arr[i-1] or arr[i] == arr[i+1]):
                return False

    if modify > 1:
        return False

    return True


if __name__ == "__main__":
    arr = [10, 5, 1]

    print(nonDecreasing(arr))
