"""
This problem was asked by Google.

Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

    a
   / \
  b   c
 /
d
"""

class Node:
    def __init__(self, key):
        self.data = key
        self.right = self.left = None

def height(root):
    if(not root):
        return 0

    leftHt = height(root.left)
    rightHt = height(root.right)

    return max(leftHt, rightHt) + 1

def deepestNode(root, levels):
    if not root:
        return

    if levels == 1:
        print(root.data)
    else:
        deepestNode(root.left, levels-1)
        deepestNode(root.right, levels-1)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.right = Node(7)
    root.right.right.right = Node(8)
    root.right.left.right.left = Node(9)

    # Calculating height of tree
    levels = height(root)

    # Printing the deepest node
    deepestNode(root, levels)
