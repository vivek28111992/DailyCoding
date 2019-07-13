"""
Knight Tours Problem
"""


class KnightTour:

    def __init__(self, n):
        # initialize the board
        self.board = [[-1] * n for _ in range(n)]

        self.n = n

        # deltas define the next move of Knight
        self.deltas = [
            (2, 1),
            (1, 2),
            (-1, 2),
            (-2, 1),
            (-2, -1),
            (-1, -2),
            (1, -2),
            (2, -1)
        ]

    def print_solution(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end=' ')
            print('\n')

    def is_safe(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n and self.board[x][y] == -1

    def solve_kt(self):
        # Since Knight is initially at the first block
        self.board[0][0] = 0

        # Start from 0, 0 and explore all tours using solveKTUtil()
        if not self.solve_kt_util(0, 0, 1):
            print('Solution does not exist')
            return False
        else:
            self.print_solution()

        return True

    def solve_kt_util(self, x, y, movei):
        print('self.board ', self.board)
        if movei == self.n * self.n:
            return True

        # Try all next moves from the current coordinate x, y
        for k in range(self.n):
            next_x = x + self.deltas[k][0]
            next_y = y + self.deltas[k][1]

            if self.is_safe(next_x, next_y):
                self.board[next_x][next_y] = movei
                if self.solve_kt_util(next_x, next_y, movei + 1):
                    return True
                else:
                    self.board[next_x][next_y] = -1  # backtracking
        return False


if __name__ == '__main__':
    kt = KnightTour(4)
    print(kt.solve_kt())
