"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.


https://www.geeksforgeeks.org/maximum-difference-between-two-elements/
https://www.geeksforgeeks.org/maximum-profit-by-buying-and-selling-a-share-at-most-k-times/
"""

# the function assumes that they are at least two elements in array. The function returns a negative value if the array is sorted in descreasing order. Returns 0 if elements are equal

def maxDiff(arr, arr_size):
    max_diff = arr[1] - arr[0]
    min_element = arr[0]

    for i in range(1, arr_size):
        if arr[i] - min_element > max_diff:
            max_diff = arr[i] - min_element

        if arr[i] < min_element:
            min_element = arr[i]

    return max_diff

arr = [9, 11, 8, 5, 7, 10]
size = len(arr)
print ("Maximum difference is", maxDiff(arr, size))
