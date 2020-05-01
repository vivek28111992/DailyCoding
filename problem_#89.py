"""
A binary search tree is a tree with two children, left and right, and satisfies the constraint that the key in the left child must be less than or equal to the root and the key in the right child must be greater than or equal to the root.
"""

import math

# A binary tree node has data, pointer to left child and a pointer to right child
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Global variable prev - to keep track of prev node during Inorder traversal
prev = None

def isBSTUtil(root):

    global prev

    # traverse the tree inorder fashion and keep track of prev node
    if (root is None):
        return True

    if (isBSTUtil(root.left) is False):
        return False

    # if prev node data is found greater than the current node's data return false
    if prev is not None and prev.data > root.data:
        return False

    #store the current node in prev
    prev = root
    return isBSTUtil(root.right)

def isBST(root):
    # prev is a global variable
    global prev
    prev = None
    return isBSTUtil(root)

root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

if isBST(root):
    print('It is a BST')
else:
    print('Not a BST')
