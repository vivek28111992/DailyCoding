"""
We're given a hashmap associating each courseId key with a list of courseIds values, which represents that the prerequisites of courseId are courseIds. Return a sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}, should return ['CSC100', 'CSC200', 'CSCS300'].
"""

import collections

class Solution(object):
    def canFinish(self, numCourses, prerequisities):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        visited = collections.defaultdict(int)

        # create graph
        for x, y in prerequisities:
            print(x, y)
            graph[x].append(y)

        # visit each node
        for c in list(graph.keys()):
            if not self.dfs(graph, visited, c):
                return False
        return True

    def dfs(self, graph, visited, v):
        print('graph ', graph)
        # if it is done visited then do not visit again
        if visited[v] == 1:
            return True
        # if ith node is marked as being visited, then cycle is found
        if visited[v] == -1:
            return False

        # mark as being visited
        visited[v] = -1

        for u in graph[v]:
            if not self.dfs(graph, visited, u):
                return False
        visited[v] = 1
        return True


if __name__ == '__main__':
    c = Solution()
    res = c.canFinish(4, [["algebra", "basics"],["trig","algebra"],["calculus","trig"]])
    print(res)