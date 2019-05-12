"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.


https://leetcode.com/problems/remove-nth-node-from-end-of-list/solution/
https://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/
"""

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # createNode and make linked list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def removeNthFromEnd(self, n):
        dummy = Node(0)
        dummy.next = self.head
        first = dummy
        second = dummy

        # Advances first pointer so that the gap between first and second is n nodes apart
        for i in range(n):
            first = first.next

        # Move first to the end, maintaining the gap
        while first.next != None:
            first = first.next
            second = second.next

        second.next = second.next.next
        return second.next.data

# Driver Code
llist = LinkedList()
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
print(llist.removeNthFromEnd(2))
