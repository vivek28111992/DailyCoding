"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
"""

def encoding(str):
    encodingObj = dict()

    for ch in str:
        if ch in encodingObj and ch == prev_ch:
            current_window += 1
            encodingObj[ch] = current_window if current_window > encodingObj[ch] else encodingObj[ch]
            prev_ch = ch
        else:
            current_window = 1
            encodingObj[ch] = encodingObj[ch] if ch in encodingObj else 1
            prev_ch = ch

    print(encodingObj)
    return encodingObj

encoding('AAAABBBCCDAA')