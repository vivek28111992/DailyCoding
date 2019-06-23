"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g


https://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/
"""

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

"""
Recursive function to construct binary of size len from Inorder traversal in[] and Preorder traversal pre[]. Initialize values of inStrt and inEnd should be 0 and len - 1. The function doesn't do any error checking for cases where inorder and preorder do not form a tree
"""
def buildTree(inOrder, preOrder, inStrt, inEnd):
    if(inStrt > inEnd):
        return None

    # Pinch current node from Preorder traversal using preIndex and increment preIndex
    tNode = Node(preOrder[buildTree.preIndex])
    buildTree.preIndex += 1

    # If this node has no children then return
    if inStrt == inEnd:
        return tNode

    # Else find the index of this node in Inorder traversal
    inIndex = search(inOrder, inStrt, inEnd, tNode.data)

    # Using index in Inorder Traversal, construct left and right subtrees
    tNode.left = buildTree(inOrder, preOrder, inStrt, inIndex-1)
    tNode.right = buildTree(inOrder, preOrder, inIndex+1, inEnd)

    return tNode

# UTILITY FUNCTIONS
# Function to find index of value in arr[start...end]
# The function assumes that value is present inOrder[]

def search(arr, start, end, value):
    for i in range(start, end + 1):
        if arr[i] == value:
            return i

def printInorder(node):
    if node is None:
        return

    # first recur on left child
    printInorder(node.left)

    # then print the data of node
    print(node.data, end=' ')

    # now recur on right child
    printInorder(node.right)



inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
# Static variable preIndex
buildTree.preIndex = 0
root = buildTree(inOrder, preOrder, 0, len(inOrder) - 1)

# Let us test the build tree by priting Inorder traversal
printInorder(root)
