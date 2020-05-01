"""
Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make the string valid (i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2, since we must remove all of them.
"""

def removeParenthesis(s):
    pstack = []

    for i in s:
        if i == ')':
            if len(pstack) == 0:
                pstack.append(i)
            elif pstack[-1] == ')':
                pstack.append(i)
            else:
                pstack.pop()
        else:
            pstack.append(i)

    return len(pstack)

if __name__ == '__main__':
    res = removeParenthesis(')(')
    print(res)
