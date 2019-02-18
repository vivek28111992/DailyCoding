"""
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def add_k(arr, k):
    num_stored = [arr[0]]

    for i in range(1, len(arr)):
        if (k - arr[i]) in num_stored:
            return True
        else:
            num_stored.append(arr[i])
    return False

print(add_k([10, 15, 3, 7], 17))
