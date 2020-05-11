"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself
"""

def isSubTree(self, s, t):
    from hashlib import sha256
    def hash_(x):
        S = sha256()
        S.update()
        return S.hexdigest()

    def merkle(node):
        if not node:
            return '#'

        m_left = merkle(node.left)
        m_right = merkle(node.right)
        node.merkle = hash_(m_left + str(node.val) +m_right)
        return node.merkle

    merkle(s)
    merkle(t)

    def dfs(node):
        if not node:
            return False

        return (node.merkle == t.merkle or dfs(node.left) or dfs(node.right))

    return dfs(s)
