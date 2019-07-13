"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.

Given N, write a function to return the number of knight's tours on an N by N chessboard.


https://www.geeksforgeeks.org/the-knights-tour-problem-backtracking-1/
https://www.dailycodingproblem.com/blog/knights-tour/
"""


def is_valid_move(board, move, n):
    r, c = move
    return 0 <= r < n and 0 <= c < n and board[r][c] is None

def valid_moves(board, row, col, n):
    deltas = [
        (2, 1),
        (1, 2),
        (1, -2),
        (-2, 1),
        (-1, 2),
        (2, -1),
        (-1, -2),
        (-2, -1)
    ]

    all_moves = [(row + r_delta, col + c_delta) for r_delta, c_delta in deltas]
    return [move for move in all_moves if is_valid_move(board, move, n)]

def knight_tours(n):
    count = 0
    for i in range(n):
        for j in range(n):
            board = [[None for _ in range(n)] for _ in range(n)]
            board[i][j] = 0
            count += knight_tours_helper(board, [(i, j)], n)
    return count

def knight_tours_helper(board, tour, n):
    if len(tour) == n:
        return 1
    else:
        count = 0
        last_r, last_c = tour[-1]
        for r, c in valid_moves(board, last_r, last_c, n):
            tour.append((r, c))
            board[r][c] = len(tour)
            count += knight_tours_helper(board, tour, n)
            tour.pop()
            board[r][c] = None
        return count

if __name__ == '__main__':
    print(knight_tours(8))