"""
Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.
"""

r = 4
c = 4

# Function to check if a word exists in a grid starting from the first match in the grid level: index till which pattern is matched x, y: current position in 2D array
def findMatch(mat, pat, x, y, nrow, ncol, level):
    l = len(pat)

    # Pattern matched
    if level == l:
        return True

    # out of boundry
    if (x < 0 or y < 0) or (x >= nrow or y >= ncol):
        return False

    # If grid matches with a letter while recursion
    if (mat[x][y] == pat[level]):

        # Marking this cell as visited
        temp = mat[x][y]
        mat[x].replace(mat[x][y], "#")

        # finding subpattern in 4 directions
        res = ((mat, pat, x - 1, y, nrow, ncol, level + 1) or
                (mat, pat, x + 1, y, nrow, ncol, level + 1) or
                (mat, pat, x, y+1, nrow, ncol, level + 1) or
                (mat, pat, x, y-1, nrow, ncol, level + 1))

        # marking this cell as unvisited again
        return res
    else: # Not matching then false
        return False


# Function to check if the word exists in the grid or not
def checkMatch(mat, pat, nrow, ncol):
    l = len(pat)

    # if total characters in matrix is less then pattern lenghth
    if (l > nrow * ncol):
        return False

    # Traverse in the grid
    for i in range(nrow):
        for j in range(ncol):
            # If the first letter matches then recur and check
            if mat[i][j] == pat[0]:
                if (findMatch(mat, pat, i, j, nrow, ncol, 0)):
                    return True
    return False


if __name__ == "__main__":

    grid = ["axmy", "bgdf","xeet", "raks"]

    # Function to check if word
    # exists or not
    if (checkMatch(grid, "geeks", r, c)):
        print("Yes")
    else:
        print("No")