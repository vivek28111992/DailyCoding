"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
get(key): gets the value at key. If no such key exists, return null.
Each operation should run in O(1) time.


https://www.geeksforgeeks.org/design-a-data-structure-for-lru-cache/
"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class LRUCache:
    def __init__(self, capacity):
        self.mapObj = dict()
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.head.pre = None
        self.tail.next = None
        self.count = 0

    def deleteNode(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def addToHead(self, node):
        node.next = self.head.next
        node.next.pre = node
        node.pre = self.head
        self.head.next = node

    # This method works in O(1)
    def get(self, key):
        if key in self.mapObj:
            node = self.mapObj[key]
            result = node.value
            self.deleteNode(node)
            self.addToHead(node)
            print("Got the value : {} for the key: {}".format(result, key))
            return result
        print('Did not get any value for the key: {}'.format(key))
        return -1

    def set(self, key, value):
        print('Going to set the (key, value) : ({}, {})'.format(key, value))
        if key in self.mapObj:
            node = self.mapObj[key]
            node.value = value
            self.deleteNode(node)
            self.addToHead(node)

        else:
            node = Node(key, value)
            self.mapObj[key] = node
            if self.count < self.capacity:
                self.count += 1
                self.addToHead(node)
            else:
                self.mapObj.pop(self.tail.pre.key, None)
                self.deleteNode(self.tail.pre)
                self.addToHead(node)

cache = LRUCache(2)

# it will store a key (1) with value 10 in the cache.
cache.set(1, 10)

# it will store a key (1) with value 10 in the cache.
cache.set(2, 20)

print('Value for the key: 1 is {}'.format(cache.get(1)))

# evicts key 2 and store a key (3) with value 30 in the cache.
cache.set(3, 30)

# returns -1 (not found)
print('Value for the key: 2 is {}'.format(cache.get(2)))

# evicts key 1 and store a key (4) with value 40 in the cache.
cache.set(4, 40)

# returns -1 (not found)
print('Value for the key: 1 is {}'.format(cache.get(1)))

# returns 30
print('Value for the key: 3 is {}'.format(cache.get(3)))

# return 40
print('Value for the key: 4 is {}'.format(cache.get(4)))