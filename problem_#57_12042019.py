"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less. You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words. If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.
"""

def breakStr(inputStr, k):

    str_arr = inputStr.split()
    line_arr = []
    remaining_space = k
    line_str = ''
    for ch in str_arr:

        if len(ch) > k:
            return None

        if len(ch) <= remaining_space:
            line_str = ch if line_str == '' else (line_str +' '+ ch)
            remaining_space -= (len(ch) + 1)
        else:
            line_arr.append(line_str)
            line_str = ch
            remaining_space = k - (len(ch) + 1)

    if len(line_str) > 0:
        line_arr.append(line_str)

    return line_arr

if __name__ == '__main__':
    assert not breakStr("encyclopedia", 8)
    assert breakStr("the quick brown fox jumps over the lazy dog", 10) == [
        "the quick", "brown fox", "jumps over", "the lazy", "dog"]
