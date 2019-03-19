"""
This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

https://github.com/nowol79/Daily_Coding_Problem/issues/16
https://www.youtube.com/watch?v=RTDWoI5FVrk
"""

def helper(arr, results, curr_house, prev_color, curr_cost, curr_sequence):
    if curr_house == len(arr):
        results.append((curr_cost, curr_sequence))
        return

    for i in range(0, len(arr)):
        if i != prev_color:
            helper(arr, results, curr_house+1, i, arr[curr_house][i] + curr_cost, curr_sequence + str(i))

def minimizeColorCost(arr):
    results = list()
    helper(arr, results, 0, -1, 0, "")
    print('res ', results)
    return min(results)

arr = [[1,2,3,4], [1,2,1,0], [6,1,1,5], [2,3,5,5]]
print(minimizeColorCost(arr))
