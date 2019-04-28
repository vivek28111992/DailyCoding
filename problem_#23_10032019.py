"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.

https://github.com/r1cc4rdo/daily_coding_problem/blob/master/daily_coding_problem_21_25.py
https://www.geeksforgeeks.org/shortest-path-in-a-binary-maze/
"""

def coding_problem_23(matrix, start, end):
    coords = [(index_r, index_c) for index_r, row in enumerate(matrix) for index_c, element in enumerate(row) if not element]
    print('coords ', coords)

    current_distance = 0

    distances = [[None for col in range(len(matrix[0]))] for row in range(len(matrix))]
    distances[start[0]][start[1]] = 0

    print('distances ', distances)

    while True:

        wavefront = [coord for coord in coords if distances[coord[0]][coord[1]] == current_distance]

        print('wavefront ', wavefront)

        if not wavefront:
            break

        print('dist ', distances)

        current_distance += 1

        for node in wavefront:

            print('node ', node)

            neighbours = [coord for coord in coords if (abs(node[0] - coord[0]) + abs(node[1] - coord[1])) == 1]
            print('neighbours ', neighbours)

            for n in neighbours:
                if distances[n[0]][n[1]] is None:
                    distances[n[0]][n[1]] = current_distance

    return distances[end[0]][end[1]]

matrix = [
            [False, False, False, False],
            [True, True, False, True],
            [False, False, False, False],
            [False, False, False, False]
        ]

print(coding_problem_23(matrix, (3, 0), (0, 0)))