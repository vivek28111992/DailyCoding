"""
You are in an infinite 2D grid where you can move in any of the 8 directions:

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

Example:

Input: [(0, 0), (1, 1), (1, 2)]
Output: 2
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
"""

# function to give minimum steps to move from p1 to p2
def shortestPath(p1, p2):

    dx = abs(p1[1] - p2[0])
    dy = abs(p2[1] - p2[0])

    return max(dx, dy)

# Function to return the minimum steps
def coverPoints(seq, size):

    stepCount = 0
    for i in range(size-1):
        stepCount += shortestPath(seq[i], seq[i+1])
    return stepCount

if __name__ == '__main__':
    arr = [[4, 6], [1, 2], [4, 5], [10, 12]]

    n = len(arr)
    print(coverPoints(arr, n))
