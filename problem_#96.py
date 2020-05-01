"""
Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

def printArr(arr):
    for i in range(len(arr)):
        print(a[i], end=" ")
    print()

def permutation(arr, size, n):

    # if size becomes 1 then prints the obtained permutation
    if size == 1:
        printArr(arr)
        return

    for i in range(size):
        permutation(arr, size-1, n)

        # if size is odd, swap first and last element
        # else If size is even, swap ith and last element
        if size & 1:
            a[0], a[size-1] = a[size-1], a[0]
        else:
            a[i], a[size - 1] = a[size - 1], a[i]

if __name__ == "__main__":
    a = [1, 2, 3, 4]
    n = len(a)
    permutation(a, n, n)
