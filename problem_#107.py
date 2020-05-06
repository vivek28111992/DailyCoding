"""
Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.

  1
 / \
2   3
   / \
  4   5
"""

class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def printBinaryTree(root):

    # Base Class
    if root is None:
        return

    # Create an empty queue for level order traversal
    q = []
    q.append(root)

    while q:
        # node count (queue size) indicates number of nodes at current level
        count = len(q)

        # Dequeue all nodes of current node
        # Enqueue all node of next level
        while count > 0:
            temp = q.pop(0)
            print(temp.val, end=' ')
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

            count -= 1
        print(' ')

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2);
    root.right = Node(3);
    root.left.left = Node(4);
    root.left.right = Node(5);
    root.right.right = Node(6);

    printBinaryTree(root)