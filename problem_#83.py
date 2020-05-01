"""
Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f
should become:

  a
 / \
 c  b
 \  / \
  f e  d
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def invert(node):
    if (node == None):
        return

    temp = node

    invert(node.left)
    invert(node.right)

    temp = node.left
    node.left = node.right
    node.right = temp

"""
Helper function to print Inorder traversal.
"""
def inOrder(node):
    if node == None:
        return

    inOrder(node.left)
    print(node.data, end=" ")
    inOrder(node.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    inOrder(root)
    print('\n')

    """ Convert tree to its mirror """
    invert(root)

    inOrder(root)

