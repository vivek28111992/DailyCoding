"""
Given a number represented by a list of digits, find the next greater permutation of a number, in terms of lexicographic ordering. If there is not greater permutation possible, return the permutation with the lowest value/ordering.

For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should return [2,1,3]. The list [3,2,1] should return [1,2,3].

Can you perform the operation without allocating extra memory (disregarding the input memory)?
"""

def findNext(number, n):
    # Start from right most digit and find the first digit that is smaller than the digit next to it
    for i in range(n-1, 0, -1):
        if number[i-1] < number[i]:
            break

    # If no such digit found, then all numbers are in descending order, no greater number is possible
    if i == 1 and number[i-1] >= number[i]:
        sorted(number)
        return number

    # Find the smallest digit on the right side of (i-1)th digit that is greater than number [i-1]
    x = number[i-1]
    smallest = i
    for j in range(i+1, n):
        if number[j] > x and number[j] < number[smallest]:
            smallest = j

    # Swapping the above found smallest digit with (i-1)'th
    number[smallest], number[i - 1] = number[i - 1], number[smallest]

    # X is the final number, in integer datatype
    x = 0
    # Converting list upto i-1 into number
    for j in range(i):
        x = x * 10 + number[j]

    # Sort the digits after i-1 in ascending order
    number = sorted(number[i:])
    # converting the remaining sorted digits into number
    for j in range(n - i):
        x = x * 10 + number[j]
    return x

if __name__ == '__main__':
    digits = "534976"
    print(findNext([5,3,4,9,7,6], len(digits)))