class LinkedList:
    def __init__(self):
        self.head = None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def reverseLL(self):
        prev = None
        next = self.head
        node = self.head
        while next is not None:
            next = node.next
            node.next = prev
            prev = node
            node = next
        self.head = prev

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return " -> ".join(nodes)

llist = LinkedList()
print(llist)

first_node = Node("a")
llist.head = first_node
print(llist)

second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node
print(llist)
llist.reverseLL()
print(llist)
