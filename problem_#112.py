"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. Assume that each node in the tree also has a pointer to its parent.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

# Finds the path from root node to given root of the tree. Stores the path in a list path[], returns true if path exists otherwise false
def findPath(root, path, k):
    # Base Case
    if root is None:
        return

    # Store this node in path. The node will be removed if not in path from root to k
    path.append(root.data)

    # See if the k is same as root's data
    if root.data == k:
        return True

    # Check if k is found in left or right sub-tree
    if ((root.left != None and findPath(root.left, path, k)) or (root.right != None and findPath(root.right, path, k))):
        return True

    # If not present in subtree rooted with root, remove root from path and return False

    path.pop()
    return False

def findLCA(root, n1, n2):

    # To store paths to n1 and n2 from the root
    path1 = []
    path2 = []

    # Find paths from root to n1 and root to n2. If either n1 or n2 is not present, return -1
    if (not findPath(root, path1, n1) or not findPath(root, path2, n2)):
        return -1

    # Compare the paths to get the first different value
    i = 0
    while (i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("LCA(2, 4) = %d" % (findLCA(root, 2, 4)))

