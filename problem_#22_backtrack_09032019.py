# A recursive program to print all possible partitions of a given string into dictionary words

# A utitlity function to check whether a word is present in dictionary or not. An array of strings is used for dictionary. Using array of strings for dictionary is definitely not a good idea. We have used for simplicity of the program.

def dictionaryContains(word):
    dictionary = ['mobile', 'samsung', 'sam', 'sung', 'man', 'mango', 'icecream', 'and', 'go', 'i', 'love', 'ice', 'cream']
    if word in dictionary:
        return True
    else:
        return False

# Prints all possible word breaks of given string
def wordBreak(str):
    wordBreakUtil(str, len(str), '')

# result store the current prefix with spaces between words
def wordBreakUtil(str, n, result):
    # Process all prefixes one by one
    for i in range(1, n+1):
        # extract substring from 0 in i in prefix
        prefix = str[:i]

        # if dictionary contains this prefix, then we check for remaining string. Otherwise we ignore this prefix (there is no else for this if) & try next
        if (dictionaryContains(prefix)):
            # if no more elements are there, print it
            if i == n:
                # add this element to previous prefix
                result += prefix
                print(result)
                return
            wordBreakUtil(str[i:], n-i, result+prefix+' ')

word = 'iloveicecreamandmango'
wordBreak(word)