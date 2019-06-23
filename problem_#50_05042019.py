"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).


https://www.geeksforgeeks.org/evaluation-of-expression-tree/
"""

# Class to represent the nodes of syntax tree
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# This function receives a node of the syntax tree and recursively evaluate it
def evaluateExpressionTree(root):

    # empty tree
    if root is None:
        return 0

    # leaf node
    if root.left is None and root.right is None:
        return int(root.data)

    # evaluate left tree
    left_sum = evaluateExpressionTree(root.left)

    # evaluate right tree
    right_sum = evaluateExpressionTree(root.right)

    # check which operation to apply
    if root.data == '+':
        return left_sum + right_sum

    elif root.data == '-':
        return left_sum - right_sum

    elif root.data == '*':
        return left_sum * right_sum

    else:
        return left_sum / right_sum

if __name__ == '__main__':
    # creating a sample tree
    root = Node('+')
    root.left = Node('*')
    root.left.left = Node('5')
    root.left.right = Node('4')
    root.right = Node('-')
    root.right.left = Node('100')
    root.right.right = Node('20')
    print(evaluateExpressionTree(root))

    root = None

    # creating a sample tree
    root = Node('+')
    root.left = Node('*')
    root.left.left = Node('5')
    root.left.right = Node('4')
    root.right = Node('-')
    root.right.left = Node('100')
    root.right.right = Node('/')
    root.right.right.left = Node('20')
    root.right.right.right = Node('2')
    print(evaluateExpressionTree(root))
