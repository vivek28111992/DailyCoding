"""
Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4
"""

MAX = 256

def compare(arr1, arr2):
    print('arr1 ', arr1)
    print('arr2 ', arr2)
    for i in range(MAX):
        if arr1[i] != arr2[i]:
            return False
    return True

# this function search for all permutations of pat[] in txt[]
def search(pat, txt):

    M = len(pat)
    N = len(txt)

    # countP[]: Store count of all characters of pattern
    # countTW[]: Store count of current window of text
    countP = [0] * MAX
    countTW = [0] * MAX

    for i in range(M):
        countP[ord(pat[i])] += 1
        countTW[ord(txt[i])] += 1

    # Traverse through remaining characters of pattern
    for i in range(M, N):
        # Compare counts of current window of txt with counts of pattern[]
        if compare(countP, countTW):
            print("Found at Index ", (i-M))

        # Add current character to current window
        countTW[ord(txt[i])] += 1

        # Remove the first character of previous window
        countTW[ord(txt[i-M])] -= 1

    # Check for the last window in text
    if compare(countP, countTW):
        print("Found at Index", N - M)

if __name__ == "__main__":
    txt = "BACDGABCDA"
    pat = "ABCD"
    search(pat, txt)


