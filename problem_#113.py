"""
Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here", return "here world hello"

Follow-up: given a mutable string representation, can you perform this operation in-place?
"""

def reverseStr(s):
    words = s.split(' ')
    revStr = []
    print('words ', words)

    for word in words:
        revStr.insert(0, word)

    print("Reversed String:")
    print(" ".join(revStr))



if __name__ == "__main__":
    reverseStr("hello world here")
