"""
Determine whether a doubly linked list is a palindrome. What if it’s singly linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False
"""

class Node:

    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev

# Given a reference (pointer to pointer) to the head of a list and an int, inserts a new node on the front of the list.
def push(head_ref, new_data):
    new_node = Node(new_data, head_ref, None)

    if head_ref != None:
        head_ref.prev = new_node
        head_ref = new_node
    return head_ref

# Function to check if list is palindrome or not
def isPalindrome(left):
    if left == None:
        return True

    # Find rightmost node
    right = left
    while right.next != None:
        right = right.next

    while left != right:
        if left.data != right.data:
            return False

        left = left.next
        right = right.prev
    return True

if __name__ == "__main__":
    head = None
    head = push(head, 'l')
    head = push(head, 'e')
    head = push(head, 'v')
    head = push(head, 'e')
    head = push(head, 'l')

    if isPalindrome(head):
        print("It is Palindrome")
    else:
        print("Not Palindrome") 


