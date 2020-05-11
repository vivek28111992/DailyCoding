"""
Given a binary tree, return the level of the tree with minimum sum.
"""

from collections import deque as d

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def minLevelSum(root):
    # Base case
    if root is None:
        return 0

    # Initialize result
    result = root.val

    q = d()
    q.append(root)

    while q:
        count = len(q)

        # Iterate for all the nodes in the queue currently
        sum = 0
        while count > 0:
            count -= 1

            # Dequeue an node from queue
            temp = q[0]
            q.popleft()

            # Add this node's value to current sum.
            sum += temp.val

            if temp.left is not None:
                q.append(temp.left)

            if temp.right is not None:
                q.append(temp.right)

        # Update the minimum node count value
        result = min(result, sum)

    return result


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(8)
    root.right.right.left = Node(6)
    root.right.right.right = Node(7)
    res = minLevelSum(root)

    print('res ', res)
