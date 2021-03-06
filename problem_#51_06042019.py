"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.


https://www.geeksforgeeks.org/shuffle-a-deck-of-cards-3/
"""

import random

# A function to generate a random permutation of arr[]
def randomize(arr, n):
    # Start from the last element and swap one & one. We don't need to run for the first element that's why i > 0
    for i in range(n-1, 0, -1):
        # Pick a random index from 0 to i
        j = random.randint(0, i+1)

        # Swap arr[i] with the element at random index
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def shuffle(card, n):


    # Initialize seed randomly
    for i in range(n):

        # Random for remaining positions
        r = i + (random.randint(0, 55) % (52 - i))
        tmp = card[i]
        card[i] = card[r]
        card[r] = tmp


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    n = len(arr)
    # print(randomize(arr, n))

    a = [0, 1, 2, 3, 4, 5, 6, 7, 8,
         9, 10, 11, 12, 13, 14, 15,
         16, 17, 18, 19, 20, 21, 22,
         23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36,
         37, 38, 39, 40, 41, 42, 43,
         44, 45, 46, 47, 48, 49, 50,
         51]
    shuffle(a, 52)
    print(a)


