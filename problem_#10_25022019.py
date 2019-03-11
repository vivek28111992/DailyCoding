""""
Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""

from threading import Timer
import time

def nArgs(*args):
    for each in args:
        print(each)

def job_scheduler(f, time):
    r = Timer(time, f, ("OWLS", "OWLS", "OWLS"))
    r.start()

def jobscheduler(f, n):
	time.sleep(n/1000)
	return f()

if __name__ == '__main__':
    job_scheduler(nArgs, 2) # first way

    print(time.ctime())
    print(jobscheduler(lambda: "Hi! " + time.ctime(), 2000)) # second way
