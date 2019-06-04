"""
https://www.geeksforgeeks.org/minimum-insertions-to-form-a-palindrome-dp-28/
"""

# A Dynamic Programming based program to find minimum number insertions needed to make a str1ing palindrome.

# A utility function to find minimum of two integers.

def Min(a, b):
    return min(a, b)

# A DP function to find minimum number of insertions
def findMinInsertionsDP(str1, n):

    # Create a table of size n*n. table[i][j] will store minimum number of insertions needed to convert str1[i..j] to a palindrome.

    table = [[0 for i in range(n)] for i in range(n)]

    # Fill the table
    for gap in range(1, n):
        l = 0
        for h in range(gap, n):
            print('l ', l)
            print('h ', h)
            if str1[l] == str1[h]:
                table[l][h] = table[l + 1][h - 1]
            else:
                table[l][h] = (Min(table[l][h - 1], table[l + 1][h]) + 1)
            print('table ', table)
            l += 1

    # Return minimum number of insertions for str1[0..n-1]
    return table[0][n - 1]


# Driver Code
str1 = "geeks"
print(findMinInsertionsDP(str1, len(str1)))

