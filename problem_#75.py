"""
This problem was asked by Microsoft.

Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
"""

def longestSubSeq(arr):
    max = -1
    max_arr = [1] * len(arr)

    for i in range(1, len(arr)):
        for j in range(len(arr)):
            if arr[j] < arr[i] and max_arr[i] < (1 + max_arr[j]):
                max_arr[i] = 1 + max_arr[j]
                max = max_arr[i] if max_arr[i] > max else max
    print(max)
    return max

if __name__ == '__main__':
    longestSubSeq([10, 22, 9, 33, 21, 50, 41, 60])


