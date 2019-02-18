"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""
import collections


class Codec:
    def buildNode(self, val):
        return None if val == 'Null' else Node(val)

    def serialize(self, root):
        queue = [root]
        for node in queue:
            if not node:
                continue
            queue += [node.left, node.right]

        return ','.join(
            map(lambda item: str(item.val) if item else 'Null', queue))

    def deserialize(self, data):
        parts = data.split(',')
        root = self.buildNode(parts[0])
        queue, i = collections.deque([root]), 1

        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = map(self.buildNode, (parts[i], parts[i + 1]))
                queue.append(node.left)
                queue.append(node.right)
                i += 2
        return root


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# a = Node('root')
# b = Node('left')
# c = Node('right')
# d = Node('left.left')
#
# a.left = b
# a.right = c
# b.left = d
#
# codec = Codec()
# s = codec.serialize(a)
# print(s)
# root = codec.deserialize(s)
# print(root)
# print(codec.serialize(root))

codec = Codec()
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert codec.deserialize(codec.serialize(node)).left.left.val == 'left.left'
