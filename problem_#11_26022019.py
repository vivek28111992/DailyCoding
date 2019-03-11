"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""
str_set = ['dog', 'deer', 'deal', 'able', 'abode', 'about', 'above', 'abuse', 'syzygy']
def suggested_word(word):
    matched_arr = []
    n = len(word)
    for i in range(len(str_set)):
        if word == str_set[i][:n]:
            matched_arr.append(str_set[i])
    return ', '.join(matched_arr)

if __name__ == '__main__':
    search_word = input('Enter word ')
    print(suggested_word(search_word))
