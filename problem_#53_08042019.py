"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.


https://www.youtube.com/watch?v=AN0axYeLue0
https://www.geeksforgeeks.org/queue-using-stacks/
https://coderbyte.com/algorithm/implement-queue-using-two-stacks
"""

# implement stacks using plain lists with push and pop functions
stack1 = []
stack2 = []

# implement enqueue method by using only stacks
# and the append and pop functions
def enqueue(element):
    stack1.append(element)

# implement dequeue method by pushing all elements
# from stack 1 into stack 2, which reverses the order
# and then popping from stack 2
def dequeue():
    if len(stack2) == 0:
        if len(stack1) == 0:
            return 'Cannot dequeue because queue is empty'
        while len(stack1) > 0:
            stack2.append(stack1.pop())
    return stack2.pop()

enqueue('a')
enqueue('b')
enqueue('c')
print(dequeue())
print(dequeue())
