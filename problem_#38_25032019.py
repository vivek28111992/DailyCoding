"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.


https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/
https://www.freecodecamp.org/news/lets-backtrack-and-save-some-queens-1f9ef6af5415/
https://www.dailycodingproblem.com/blog/an-introduction-to-backtracking/
"""

def n_queens(n, board=[]):
    if n == len(board):
        return 1

    count = 0
    for col in range(n):
        board.append(col)
        if is_valid(board):
            count += n_queens(n, board)

        board.pop()
    return count

def is_valid(board):
    current_queen_row, current_queen_col = len(board) - 1, board[-1]

    # Check if any queens can attack the last queen
    for row, col in enumerate(board[:-1]):
        diff = abs(current_queen_col - col)
        if diff == 0 or diff == current_queen_row - row:
            return False

    return True

for i in range(10):
    print(n_queens(i))
