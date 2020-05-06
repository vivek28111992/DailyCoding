"""
Given a list of integers and a number K, return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
"""

def contiguousEle(arr, k):
    curr_sum = arr[0]
    start_sliding = 0

    # Add elements one by one to curr_sum and if the curr_sum exceeds the sum, then remove starting element
    i = 1
    while i <= len(arr):
        # If curr_sum exceeds the sum, then remove the starting elements
        while curr_sum > k and start_sliding < i:
            curr_sum = curr_sum - arr[start_sliding]
            start_sliding += 1

        # If curr_sum becomes equal to sum, then return true
        if curr_sum == k:
            print("Sum found from indexes")
            print("%d to %d" % (start_sliding, i - 1))
            return 1

        # Add this element to curr_sum
        if i < len(arr):
            curr_sum = curr_sum + arr[i]
        i += 1

    # If we reach here,  then no subarray
    print("No subarray found")
    return 0

if __name__ == "__main__":
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    k = 14
    contiguousEle(arr, k)