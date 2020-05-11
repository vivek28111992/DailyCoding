"""
Given a string and a set of delimiters, reverse the words in the string while maintaining the relative order of the delimiters. For example, given "hello/world:here", return "here/world:hello"

Follow-up: Does your solution work for the following cases: "hello/world:here/", "hello//world:here"
"""

import re

def splitnonalpha(s):
   pos = 0
   res = []
   str = ''
   while pos < len(s):
      if not s[pos].isalpha() and str != '':
          res.append(str)
          str = ''
      elif s[pos].isalpha():
          str += s[pos]
      pos += 1

   if str != '':
        res.append(str)

   return res

def reverseStr(string):
    s = splitnonalpha(string)
    l = re.split('[a-zA-Z]', string)
    index = len(s)-1

    isalpha = False
    res = []
    for i in range(len(l)):
        if l[i] == '':
            isalpha = True
        else:
            if isalpha:
                res.append(s[index])
                index -= 1
            isalpha = False
            res.append(l[i])

    if isalpha:
        res.append(s[index])

    return res


if __name__ == "__main__":
    string = "hello/world:here/"
    print("Input string: ", string)
    string = reverseStr(string)
    print("Output string: ", "".join(string))
