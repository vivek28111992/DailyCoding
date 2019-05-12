"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

s = {')': '(', ']': '[', '}': '{'}

def isbalancedBrackets(sampleStr):
    stack = []
    for ch in sampleStr:
        if ch in s:
            if stack[-1] == s[ch]:
                stack.pop()
            else:
                stack.append(ch)
        else:
            stack.append(ch)

    if len(stack) > 0:
        return False
    else:
        return True

print(isbalancedBrackets('([)]'))