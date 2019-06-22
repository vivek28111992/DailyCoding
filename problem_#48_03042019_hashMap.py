
# A binary tree Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Recursive function to construct binary of size len from Inorder traversal in[] and Preorder traversal pre[]. Initial values of inStrt and inEnd should be 0 and len -1. The function doesn't do any error checking for cases where inorder and preorder do not form a tree

def buildTree(inOrder, pre, inStrt, inEnd, mp):

    if inStrt > inEnd:
        return None

    treeIndx = buildTree.preIndex
    tNode = Node(pre[treeIndx])
    buildTree.preIndex += 1

    # Pick current node from Preorder traversal using preIndex and increment preIndex
    if inStrt == inEnd:
        return tNode

    # Else find the index of this node in Inorder traversal
    inIndex = mp[pre[treeIndx]]

    # Using index in Inorder traversal, construct left and right subtress
    tNode.left = buildTree(inOrder, pre, inStrt, inIndex - 1, mp)
    tNode.right = buildTree(inOrder, pre, inIndex + 1, inEnd, mp)

    return tNode

def buildTreeWrap(inOrder, pre, len):
    # Store indexes of all items so that we can quickly find later
    mp = dict()
    for i in range(len):
        mp[inOrder[i]] = i

    print('mp ', mp)

    return buildTree(inOrder, pre, 0, len-1, mp)

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
root = buildTreeWrap(inOrder, preOrder, len(inOrder))

# Let us test the build tree by priting Inorder traversal
printInorder(root)