"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

https://www.youtube.com/watch?v=RHFrVNmlyA8
"""

def longestStr(s, k):
    maxlen = 0
    d = dict()
    s_ptr = 0
    for i in range(len(s)):
        if s[i] not in d.keys():
            d[s[i]] = 1
        else:
            d[s[i]] += 1

        while len(d) > k:
            d[s[s_ptr]] -= 1
            if d[s[s_ptr]] == 0:
                d.pop(s[s_ptr])
            s_ptr += 1

        maxlen = max(maxlen, i - s_ptr + 1)

    return maxlen

if __name__ == '__main__':
    print(longestStr('aabbcc', 2))
