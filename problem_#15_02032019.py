"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability

https://galaiko.rocks/posts/probability/
"""
import random

def solution(stream):
    lastprob = 0
    result = ''
    for i in range(len(stream)):
        prob = random.uniform(0, 1)
        print(prob)
        if prob > lastprob:
            result = stream[i]
            lastprob = prob
        res = result
    return res

if __name__ == '__main__':
    print(solution(['hdf', 'jdjh', 'sadgh']))