"""
A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number
"""

def findNthPerfect(n):
    count = 0
    curr = 19
    while True:
        # Find sum of digits in current no.
        sum = 0
        x = curr
        while x > 0:
            sum += x % 10
            x = int(x/10)

        # If sum is 10, we increment count
        if sum == 10:
            count += 1

        # If count becomes n, we return current number
        if count == n:
            return curr

        curr += 9

    return -1

# Driver Code
print(findNthPerfect(5))
