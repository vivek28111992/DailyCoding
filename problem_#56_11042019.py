"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given an undirected graph represented as an adjacency matrix and an integer k, write a function to determine whether each vertex in the graph can be colored such that no two adjacent vertices share the same color using at most k colors.


https://www.geeksforgeeks.org/m-coloring-problem-backtracking-5/
"""


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    # A utility function to check if the current color assignment is safe for vertex v
    def isSafe(self, v, colour, c):
        print('v ', v)
        print('color ', colour)
        print('c ', c)
        print('graph ', self.graph)
        print('------------------')
        for i in range(self.V):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True

    # A recursive utility function to solve m coloring problem
    def graphColourUtil(self, noOfColor, colour, v):
        if v == self.V:
            return True

        for c in range(1, noOfColor+1):
            if self.isSafe(v, colour, c) == True:
                colour[v] = c
                if self.graphColourUtil(noOfColor, colour, v+1) == True:
                    return True
                colour[v] = 0

    # Main function for graph Coloring
    def graphColouring(self, noOfColor):
        colour = [0] * self.V

        if self.graphColourUtil(noOfColor, colour, 0) == None:
            return False

        # Print the solution
        print("Solution exist and Following are the assigned colours:")
        for c in colour:
            print(c, end=', ')
        return True






if __name__ == '__main__':
    g = Graph(4)
    g.graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
    noOfColor = 3
    g.graphColouring(noOfColor)
