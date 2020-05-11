"""
Given a binary tree, return all paths from the root to leaves.

For example, given the tree:

   1
  / \
 2   3
    / \
   4   5
Return [[1, 2], [1, 3, 4], [1, 3, 5]].
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def printRoute(stack, root):
    if root is None:
        return

    # append this node to the path array
    stack.append(root.data)
    if (root.left == None and root.right == None):
        # print out all of its root - to - leaf
        print(' '.join([str(i) for i in stack]))

    # otherwise try both subtrees
    printRoute(stack, root.left)
    printRoute(stack, root.right)
    stack.pop()

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(2)
    printRoute([], root)