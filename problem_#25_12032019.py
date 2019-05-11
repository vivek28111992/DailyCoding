"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Implement regular expression matching with the following special characters:

. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element
That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.


https://www.geeksforgeeks.org/wildcard-character-matching/
"""

# Python program to match wild card characters

# The main function that checks if two given strings match.
# The first string may contain wildcard characters

def match(first, second):

    # if we reach at the end of both strings, we are done
    if len(first) == 0 and len(second) == 0:
        return True

    # Make sure that the characters after '*' are present
    # in second string. This function assumes that the first
    # string will not contain two consecutive '*'
    if len(first) > 1 and first[0] == '*' and len(second) == 0:
        return False

    # if the first string contains '?', or current characters of both strings match
    if (len(first) > 1 and first[0] == '?') or (len(first) != 0 and len(second) != 0 and first[0] == second[0]):
        return match(first[1:], second[1:])

    # if there is *, then there are two possibilities
    # a) We consider current character of second string
    # b) We ignore current character of second string
    if len(first) != 0 and first[0] == '*':
        return match(first[1:], second) or match(first, second[1:])

    return False

# A function to run test cases
def test(first, second):
    if match(first, second):
        print("Yes")
    else:
        print("No")

# Driver program
test("g*ks", "geeks") # Yes
test("ge?ks*", "geeksforgeeks") # Yes
test("g*k", "gee") # No because 'k' is not in second
test("*pqrs", "pqrst") # No because 't' is not in first
test("abc*bcd", "abcdhghgbcd") # Yes
test("abc*c?d", "abcd") # No because second must have 2 instances of 'c'
test("*c*d", "abcd") # Yes
test("*?c*d", "abcd") # Yes