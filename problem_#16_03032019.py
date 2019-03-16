"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.

https://github.com/r1cc4rdo/daily_coding_problem/blob/master/daily_coding_problem_16_20.py
"""

class OrderLog:

    def __init__(self, num):
        self.circular_buffer = [None] * num
        self.current_index = 0

    def record(self, order_id):
        self.circular_buffer[self.current_index] = order_id
        self.current_index += 1
        if self.current_index == len(self.circular_buffer):
            self.current_index = 0

    def get_last(self, num):
        start_index = self.current_index - num
        if start_index < 0:
            return self.circular_buffer[start_index:] + self.circular_buffer[:self.current_index]
        else:
            return self.circular_buffer[start_index:self.circular_index]

if __name__ == '__main__':
    log = OrderLog(10)
    for id in range(20):
        log.record(id)

    print(log.get_last(6))
