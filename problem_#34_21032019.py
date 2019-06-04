"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Quora.

Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".

https://github.com/r1cc4rdo/daily_coding_problem/blob/master/daily_coding_problem_31_35.py
"""

def coding_problem_34(s):

    def recurse(palindrome, before, after):
        if not before or not after:
            return after[::-1] + before + palindrome + before[::-1] + after

        if before[-1] == after[0]:
            return recurse(after[0] + palindrome + after[0], before[:-1], after[1:])

        from_before = recurse(before[-1] + palindrome + before[-1], before[:-1], after)
        from_after = recurse(after[0] + palindrome + after[0], before, after[1:])
        if len(from_before) == len(from_after):
            return min(from_before, from_after) # same length, pick lexicographically smaller

        return (from_before, from_after)[len(from_before) > len(from_after)] # pick shortest

    def pivots(word):
        for index in range(len(word)):
            yield (word[index], word[:index], word[index+1:])

        for index in range(1, len(word)):
            yield ('', word[:index], word[index:])

    candidates = [recurse(palindrome, before, after) for palindrome, before, after in pivots(s)]

    print('candidates ', candidates)

    return min(filter(lambda candidate: len(candidate) == min(map(len, candidates)), candidates))


print(coding_problem_34('race'))
