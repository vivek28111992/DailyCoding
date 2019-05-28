"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.

https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm
https://github.com/Jedshady/daily-coding-problem/blob/master/Problem%2031-60/problem_31.py
https://lawrencewu.me/2015/02/15/levenshtein-distance.html
https://rosettacode.org/wiki/Levenshtein_distance
https://www.youtube.com/watch?v=2veeHbRQUuw
"""

def editDistance(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n+1) for i in range(m+1)]

    for i in range(n+1):
        dp[0][i] = i

    for j in range(m+1):
        dp[j][0] = j



    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

    print('dp ', dp)

    return dp[m][n]



print(editDistance('kitten', 'sitting'))

