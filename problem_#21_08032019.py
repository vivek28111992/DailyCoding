"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/
"""

from operator import itemgetter
from itertools import chain

def noOfRooms():
    data = [(30, 75), (0, 50), (60, 150)]
    lectures_start = list(list(zip(*data))[0])
    lectures_start.sort()

    lectures_end = list(list(zip(*data))[1])
    lectures_end.sort()

    rooms_req = 0
    j = 0
    i = 0
    max_rooms = 0
    n = len(lectures_start)
    while i < n and j < n:
        if lectures_start[i] < lectures_end[j]:
            rooms_req += 1
            max_rooms = rooms_req if rooms_req > max_rooms else max_rooms
            i += 1
        else:
            while lectures_end[j] < lectures_start[i]:
                rooms_req -= 1
                j += 1
    print(max_rooms)

    # data = list(chain.from_iterable(data))
    #
    # print(data)
    # data = sorted(data, key=itemgetter(0))
    # print(data)

noOfRooms()
