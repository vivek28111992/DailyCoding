"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
Each method should run in constant time.


https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/
https://www.geeksforgeeks.org/design-and-implement-special-stack-data-structure/
"""

# Class to make a Node
class Node:
    # Constructor which assign argument to node's value
    def __init__(self, value):
        self.value = value
        self.next = None

    # This method returns the string representation of the object
    def __str__(self):
        return "Node({})".format(self.value)

    # __repr__ is same as __str__
    __repr__ = __str__

class Stack:
    # Stack Constructor initialise top of stack and counter
    def __init__(self):
        self.top = None
        self.maximum = None
        self.count = 0
        self.minimum = None

    # This method returns the string representation of the object (stack).
    def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = '\n'.join(out)
        return ('Top {} \n\nStack :\n{}'.format(self.top, out))

    # __repr__ is same as __str__
    __repr__ = __str__

    # This method is used to get minimum element of stack
    def getMin(self):
        if self.top is None:
            return "Stack is Empty"
        else:
            print("Minimum element in the stack is: {}".format(self.minimum.value))

    # This method is used to get minimum element of stack
    def getMax(self):
        if self.top is None:
            return "Stack is Empty"
        else:
            print("Maximum element in the stack is: {}".format(self.maximum.value))

    # Method to check if stack is Empty or not
    def isEmpty(self):
        # If top equals to None then stack is empty
        if self.top == None:
            return True
        else:
            # If top not equal to None then stack is empty
            return False

    def push(self, value):
        if self.top is None:
            self.top = Node(value)
            self.top.value = value
            self.minimum = Node(value)
            self.minimum.value = value
            self.maximum = Node(value)
            self.maximum.value = value

        elif value < self.minimum.value:
            new_node = Node(value)
            new_node_min = Node(value)
            new_node_max = Node(self.maximum.value)
            new_node.next = self.top
            new_node_max.next = self.maximum
            new_node_min.next = self.minimum
            self.top = new_node
            self.top.value = value
            self.maximum = new_node_max
            self.maximum.value = value
            self.minimum = new_node_min
            self.minimum.value = value

        elif value > self.maximum.value:
            new_node = Node(value)
            new_node_max = Node(value)
            new_node_min = Node(self.minimum.value)
            new_node.next = self.top
            new_node_max.next = self.maximum
            new_node_min.next = self.minimum
            self.top = new_node
            self.top.value = value
            self.maximum = new_node_max
            self.maximum.value = value
            self.minimum = new_node_min
            self.minimum.value = value

        else:
            new_node = Node(value)
            new_node_max = Node(self.maximum.value)
            new_node_min = Node(self.minimum.value)
            new_node.next = self.top
            new_node_max.next = self.maximum
            new_node_min.next = self.minimum
            self.maximum = new_node_max
            self.maximum.value = value
            self.minimum = new_node_min
            self.minimum.value = value
            self.top = new_node
            self.top.value = value
        print("Number Inserted: {}".format(value))

    # This method is used to pop top of stack
    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            removedNode = self.top.value
            self.top = self.top.next
            self.minimum = self.minimum.next
            self.maximum = self.maximum.next
            print("Top Most Element Removed : {}".format(removedNode))


stack = Stack()

stack.push(3)
stack.push(5)
stack.getMin()
stack.getMax()
stack.push(2)
stack.push(1)
stack.getMin()
stack.getMax()
stack.pop()
stack.getMin()
stack.getMax()
stack.pop()

