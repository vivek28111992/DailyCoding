"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add up to the same sum.
"""

def isSplitable(arr):
    arr.sort()

    total_sum = sum(map(lambda x: x, arr))
    req_sum = total_sum / 2

    if total_sum % 2 != 0:
        return False
    else:
        curr_sum = 0
        for i in range(len(arr)):
            curr_sum += arr[i]
            if curr_sum == req_sum:
                return True
        return False

if __name__ == '__main__':
    print(isSplitable([15, 5, 20, 10, 35]))
