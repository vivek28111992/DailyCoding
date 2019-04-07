"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49846/python-solution-for-intersection-of-two-singly-linked-lists
https://www.youtube.com/watch?v=l936ym8yDSo
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next

    def getCount(self):
        current = self.head
        count = 0

        # Loop while end of linked list is not reached
        while current is not None:
            count += 1
            current = current.next
        return count


def findMergeNode(list1, list2):
    headA = list1.head
    headB = list2.head
    curA = list1.head
    curB = list2.head
    while not curA.data == curB.data:
        if curA.next is None:
            curA = headB
        else:
            curA = curA.next

        if curB.next is None:
            curB = headA
        else:
            curB = curB.next
    return curA.data


if __name__ == '__main__':
    a_llist = LinkedList()
    a_llist.append(1)
    a_llist.append(2)
    a_llist.append(3)
    a_llist.append(4)
    a_llist.append(8)
    a_llist.append(9)
    a_llist.append(10)

    print('The linked list: ', end='')
    a_llist.display()
    print('\n')

    b_llist = LinkedList()
    b_llist.append(6)
    b_llist.append(7)
    b_llist.append(8)
    b_llist.append(9)
    b_llist.append(10)

    print('The linked list: ', end='')
    b_llist.display()
    print('\n')

    # print(b_llist.getCount())
    # print('\n')

    print(findMergeNode(a_llist, b_llist))