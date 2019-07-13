"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]

You should print out the following:
1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12


https://www.youtube.com/watch?v=siKFOI8PNKM
https://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/
"""


def spiral_matrix(r, c, matrix):
    k = 0  # starting row index
    m = r - 1  # ending row index
    l = c - 1  # starting column index
    n = 0  # ending column index

    d = 0  # 0 -> l to r, 1 -> t to d, 2 -> r to l, 3 -> d to t

    while k <= m and l >= n:
        if d == 0:
            for i in range(l+1):
                print(matrix[k][i], end=' ')
            k += 1
        elif d == 1:
            for i in range(k, m+1):
                print(matrix[i][l], end=' ')
            l -= 1
        elif d == 2:
            for i in range(l, n - 1, -1):
                print(matrix[m][i], end=' ')
            m -= 1
        else:
            for i in range(m, k + 1, -1):
                print(matrix[i][n], end=' ')
            n -= 1
        d = (d + 1) % 4


if __name__ == '__main__':
    a = [[1, 2, 3, 4, 5, 6],
         [7, 8, 9, 10, 11, 12],
         [13, 14, 15, 16, 17, 18]]

    R = 3
    C = 6
    spiral_matrix(R, C, a)
