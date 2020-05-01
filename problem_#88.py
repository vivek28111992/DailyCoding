"""
Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder
"""

def quotient(num, divisor):
    if num < divisor:
        return 0

    curr_num = quotient = 0
    while curr_num + divisor <= num:
        curr_num += divisor
        quotient += 1

    return quotient

if __name__ == '__main__':
    res = quotient(96, 10)
    print(res)