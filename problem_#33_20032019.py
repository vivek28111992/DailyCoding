"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2


https://leetcode.com/problems/find-median-from-data-stream/discuss/74062/Short-simple-JavaC%2B%2BPython-O(log-n)-%2B-O(1)
https://www.youtube.com/watch?v=VmogG01IjYc

https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
"""

from heapq import *

class MedianFinder:

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0

mf = MedianFinder()

arr = [2, 1, 5, 7, 2, 0, 5]
for i in range(len(arr)):
    mf.addNum(arr[i])

    print(mf.findMedian())