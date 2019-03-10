"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

https://www.geeksforgeeks.org/count-possible-decodings-given-digit-sequence/
"""


# A Dynamic Programming based
# Python3 implementation to count decodings

# A Dynamic Programming based
# function to count decodings
def helper_dp(data, k, memo):
    if k == 0:
        return 1

    s = len(data) - k       # starting index of letters which we are examing
    
    if data[s] == '0':
        return 0

    if memo[k] != None:
        return memo[k]

    result = helper_dp(data, k-1, memo)
    if k >= 2 and int(data[s:s+2]) <= 26:
        result += helper_dp(data, k-2, memo)
    memo[k] = result
    return result

def num_ways_dp(data):
    k = len(data)
    memo = [None] * (k+1)
    return helper_dp(data, k, memo)

if __name__ == '__main__':
    print(num_ways_dp('111'))
