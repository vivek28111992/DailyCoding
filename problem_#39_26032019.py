"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Dropbox.

Conway's Game of Life takes place on an infinite two-dimensional board of square cells. Each cell is either dead or alive, and at each tick, the following rules apply:

Any live cell with less than two live neighbours dies.
Any live cell with two or three live neighbours remains living.
Any live cell with more than three live neighbours dies.
Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates and the number of steps it should run for. Once initialized, it should print out the board state at each step. Since it's an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).


https://www.geeksforgeeks.org/program-for-conways-game-of-life/
"""

class GameOfLife:
    def __init__(self):
        grid = [ [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 1, 1, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 1, 1, 0, 0, 0, 0, 0 ],
            [ 0, 0, 1, 1, 0, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0 ],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
        ]

        # Displaying the grid
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 0:
                    print('.', end=' ')
                else:
                    print('*', end=' ')
            print('\n')

        self.nextGeneration(grid, 10, 10)

    def nextGeneration(self, grid, M, N):
        future = [[0 for i in range(M)] for j in range(N)]

        # Loop through every cell
        for i in range(1, M-1):
            for j in range(1, N-1):
                # finding no Of Neighbours that are alive
                aliveNeighbours = 0

                for k in range(-1, 2):
                    for l in range(-1, 2):
                        aliveNeighbours += grid[i + k][j + l]

                # The cell needs to be subtracted from its neighbours as it was counted before
                aliveNeighbours -= grid[i][j]

                # Implementing the Rules of Life

                # Cell is lonely and dies
                if ((grid[i][j] == 1) and (aliveNeighbours < 2)):
                    future[i][j] = 0

                elif ((grid[i][j] == 1) and (aliveNeighbours == 2 or aliveNeighbours == 3)):
                    future[i][j] = 1

                # Cell dies due to over population
                elif ((grid[i][j] == 1) and (aliveNeighbours > 3)):
                    future[i][j] = 0

                # A new cell is born
                elif ((grid[i][j] == 0) and (aliveNeighbours == 3)):
                    future[i][j] = 1

                # Remains the same
                else:
                    future[i][j] = grid[i][j]

        print('Next Generation \n')
        for i in range(M):
            for j in range(M):
                if future[i][j] == 0:
                    print('.', end=' ')
                else:
                    print('*', end=' ')
            print('\n')


gameOfLife = GameOfLife()
