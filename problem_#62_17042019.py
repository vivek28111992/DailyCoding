"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

Right, then down
Down, then right
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.


https://www.geeksforgeeks.org/count-possible-paths-top-left-bottom-right-nxm-matrix/
https://www.youtube.com/watch?v=GO5QHC_BmvM
"""

def nWays(n, m):
    nWaysArr = [[0] * m for _ in range(n)]

    for i in range(n):

        for j in range(m):
            if i == 0:
                nWaysArr[i][j] = 1
            elif j == 0:
                nWaysArr[i][j] = 1
            else:
                nWaysArr[i][j] = nWaysArr[i][j-1] + nWaysArr[i-1][j]

    return nWaysArr[n-1][m-1]


if __name__ == '__main__':
    print(nWays(3, 3))
