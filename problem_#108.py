"""
Given two strings A and B, return whether or not A can be shifted some number of times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false
"""

class Solution:
    def rotateString(self, A, B):
        N = len(A)
        if N != len(B):
            return False

        if N == 0:
            return True

        # Compute shift table
        shifts = [1] * (N+1)
        left = -1

        for right in range(N):
            while left >= 0 and B[left] != B[right]:
                left -= shifts[left]

            shifts[right + 1] = right - left
            left += 1
            print('left ', left)
            print('right ', right)
            print('shifts ', shifts)

        # Find match of B in A+A
        match_len = 0
        for char in A + A:
            while match_len >= 0 and B[match_len] != char:
                match_len -= shifts[match_len]

            match_len += 1
            if match_len == N:
                return True

        return False

if __name__ == '__main__':
    s = Solution()
    print(s.rotateString('abc', 'acb'))
