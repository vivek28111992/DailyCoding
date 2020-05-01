"""
Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
"""

ph_mapping = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"],
              "6":["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

def digitToLetterMapping(num):
    if(len(num)) == 0:
        return []
    elif(len(num)) == 1:
        return list(ph_mapping[num[0]])

    prev = digitToLetterMapping(num[:-1])
    additional = ph_mapping[num[-1]]
    return [s + c for s in prev for c in additional]

if __name__ == '__main__':
    print(digitToLetterMapping("23"))
