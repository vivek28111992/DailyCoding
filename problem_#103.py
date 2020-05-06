"""
Given a string and a set of characters, return the shortest substring containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

If there is no substring containing all the characters in the set, return null.
"""

no_of_chars = 256

# Function to find smallest window containing all character of pattern
def findString(string, pat):
    str_len = len(string)
    pat_len = len(pat)

    # check if string's length is less than pattern's length. If yes then no such window can exist
    if str_len < pat_len:
        print("No such window exists")
        return ""

    hash_pat = [0] * no_of_chars
    hash_str = [0] * no_of_chars

    # store occurence of characters of pattern
    for i in range(0, pat_len):
        hash_pat[ord(pat[i])] += 1
    print(hash_pat)

    start, start_index, min_len = 0, -1, float("inf")

    # start traversing the string
    count = 0 # count of character
    for j in range(0, str_len):
        # count occurence of characters of string
        hash_str[ord(string[j])] += 1

        # If string's char matches with pattern's char then increment count
        if (hash_pat[ord(string[j])] != 0 and hash_str[ord(string[j])] <= hash_pat[ord(string[j])]):
            count += 1

        # if all the character are matched
        if count == pat_len:
            # Try to minimize the window i.e., check if any character is occurring more no. of times than its occurrence in pattern then remove it from starting and also remove the useless characters.
            while (hash_str[ord(string[start])] > hash_pat[ord(string[start])] or hash_pat[ord(string[start])] == 0):
                if (hash_str[ord(string[start])] > hash_pat[ord(string[start])]):
                    hash_str[ord(string[start])] -= 1
                start += 1
                print("start ", start)

            # update window size
            len_window = j - (start + 1)
            print("len_window ", len_window)
            if min_len > len_window:
                min_len = len_window
                start_index = start

    print('start_index ', start_index)
    # If no window found
    if start_index == -1:
        print("No such window exists")
        return ""

    # Return substring starting from start_index and length min_len
    return string[start_index: start_index + len_window]

if __name__ == "__main__":
    string = "this is a test string"
    pat = "tist"

    print("Smallest window is : ")
    print(findString(string, pat))
