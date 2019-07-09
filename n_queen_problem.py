"""
N-Queen Problem
"""


class NQueensBT:

    def __init__(self, n):
        self.solution = [[0]*n for _ in range(n)]
        print(self.solution)

    # check if queen can be placed at matrix[row][column]
    def can_place(self, row, column):
        # since we are filling one column at a time,
        # we will check if no queen is placed in that particular row
        for i in range(column):
            if self.solution[row][i] == 1:
                return False

        # check for upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
            if self.solution[i][j] == 1:
                return False

        # check for lower diagonal on left side
        for i, j in zip(range(row, len(self.solution)), range(column, -1, -1)):
            if self.solution[i][j] == 1:
                return False

        return True

    def place_queen(self, queen, n):
        if queen == n:
            # if we are here that means we have solved the problem
            return True

        for row in range(n):
            # check if queen can be placed in row, col
            if self.can_place(row, queen):
                # place the queen
                self.solution[row][queen] = 1

                # solve  for next queen
                if self.place_queen(queen+1, n):
                    return True

                # if we are here that means above placement didn't work
                # BACKTRACK
                self.solution[row][queen] = 0

        return False

    def solve(self, n):
        if self.place_queen(0, n):
            # print the result
            for i in range(n):
                for j in range(n):
                    print(self.solution[i][j], end=' ')
                print("\n")
        else:
            print("NO SOLUTION EXISTS")


if __name__ == '__main__':
    nQueen = NQueensBT(4)
    nQueen.solve(4)
