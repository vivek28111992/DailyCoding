"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

 https://repl.it/@ChrisALee/8-Unival-Trees
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def solutionH(root, ans):
    if not root:
        return True

    left = solutionH(root.left, ans)

    right = solutionH(root.right, ans)

    if right and left:
        if root.left and root.left.val != root.val:
            return False

        if root.right and root.right.val != root.val:
            return False

        ans[0] += 1
        return True
    return False

def solution(root):
    ans = [0]
    solutionH(root, ans)
    return ans[0]

if __name__ == '__main__':
    root = Node(1)
    root2 = Node(2)
    root3 = Node(1)
    root4 = Node(2)
    root5 = Node(2)
    root6 = Node(2)
    root7 = Node(3)
    root8 = Node(3)
    root9 = Node(3)
    root10 = Node(1)
    root.left = root2
    root2.left = root3
    root2.right = root4
    root4.left = root5
    root4.right = root6
    root.right = root7
    root7.left = root8
    root7.right = root9
    root9.left = root10

    print(solution(root))
