"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""

def largestElem(arr):
    s = set(arr)
    m = 0
    for i in range(len(arr)):
        if arr[i]+1 in s:
            j = arr[i]
            m1 = 0
            while j in s:
                j += 1
                m1 += 1
                m = max(m, m1)
    print(m)
    return m

if __name__ == "__main__":
    largestElem([100, 4, 200, 1, 3, 2])
