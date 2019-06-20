"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.


http://allhackerranksolutions.blogspot.com/2019/02/merge-sort-counting-inversions-hacker.html
https://runzhuoli.me/2018/09/06/count-inversions-in-an-array.html
http://juliachencoding.blogspot.com/2016/08/count-inversions-extended-merge-sort.html
"""

def inversions(arr):
    n = len(arr)
    if n == 1:
        return 0
    n1 = n//2
    n2 = n - n1
    arr1 = arr[:n1]
    arr2 = arr[n1:]
    ans = inversions(arr1) + inversions(arr2)
    i1 = 0
    i2 = 0
    for i in range(n):
        if i1 < n1 and (i2 >= n2 or arr1[i1] <= arr2[i2]):
            arr[i] = arr1[i1]
            ans += i2
            i1 += 1
        elif i2 < n2:
            arr[i] = arr2[i2]
            i2 += 1
    return ans

print(inversions([2, 4, 1, 3, 5]))