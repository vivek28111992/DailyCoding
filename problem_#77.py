"""
This problem was asked by Snapchat.

Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
"""

def mergeIntervals(arr):
    arr.sort(key=lambda a: a[0], reverse=True)
    print(arr)

    res = []
    for i, e in enumerate(arr):
        if i == 0:
            curr_min, curr_max = e[0], e[1]
        else:
            if e[1] >= curr_min:
                curr_max = e[1] if e[1] > curr_max else curr_max
                curr_min = e[0] if e[0] < curr_min else curr_min
            else:
                res.append((curr_min, curr_max))
                curr_min = e[0]
                curr_max = e[1]
    res.append((curr_min, curr_max))
    return res



if __name__ == '__main__':
    print(mergeIntervals([(6, 8), (1, 9), (2, 4), (4, 7)]))
