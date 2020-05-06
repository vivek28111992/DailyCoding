"""
Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.

A solution will always exist. See Goldbach’s conjecture.

Example:

Input: 4
Output: 2 + 2 = 4
If there are more than one solution possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then

[a, b] < [c, d]
If a < c OR a==c AND b < d.
"""

def sieveOfEratosthenes(n, isPrime):
    # Initialize all entries of boolean array as True. A value in isPrime[i] will finally be False if i is not a Prime, else Ture bool isPrime[n+1]
    isPrime[0] = isPrime[1] = False
    for i in range(2, n+1):
        isPrime[i] = True

    p = 2
    while p*p <= n:
        # If isPrime[p] is not changed, then it is a Prime
        if (isPrime[p] == True):
            # Update all multiples of p
            i = p * p
            while i <= n:
                isPrime[i] = False
                i += p
        p += 1

def findPrimePair(n):

    # Generating primes using Sieve
    isPrime = [0] * (n+1)
    sieveOfEratosthenes(n, isPrime)

    # Traversing all numbers to find first pair
    for i in  range(n):
        if (isPrime[i] and isPrime[n-i]):
            return (i, (n-i))

if __name__ == "__main__":
    n = 74
    print(findPrimePair(n))
