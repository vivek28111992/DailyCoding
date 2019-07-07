"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.


https://www.geeksforgeeks.org/search-a-word-in-a-2d-grid-of-characters/
"""

def wordPresent(matrix, word):

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == (len(matrix) - 1):
                # check for only left to right
                if matrix[i][j] == word[:1]:
                    l = j + 1
                    counter = 1
                    matchWord = matrix[i][j]
                    while l < len(matrix[i]):
                        if matrix[i][l] == word[counter]:
                            matchWord += matrix[i][l]
                            if matchWord == word:
                                return True
                        else:
                            break
                        l += 1
                        counter += 1

            elif j == (len(matrix[i]) - 1):
                # check for only down
                if matrix[i][j] == word[:1]:
                    # check down
                    d = i+1
                    counter = 1
                    matchWord = matrix[i][j]
                    while d < len(matrix):
                        if matrix[d][j] == word[counter]:
                            matchWord += matrix[d][j]
                            if matchWord == word:
                                return True
                        else:
                            break
                        d += 1
                        counter += 1
            else:
                if matrix[i][j] == word[:1]:
                    d = i+1
                    l = j+1
                    counter = 1
                    matchWord = matrix[i][j]
                    # check down
                    while d < len(matrix):
                        if matrix[d][j] == word[counter]:
                            matchWord += matrix[d][j]
                            if matchWord == word:
                                return True
                        else:
                            break
                        d += 1
                        counter += 1

                    while l < len(matrix[i]):
                        if matrix[i][l] == word[counter]:
                            matchWord += matrix[i][l]
                            if matchWord == word:
                                return True
                        else:
                            break
                        l += 1
                        counter += 1
    return False

if __name__ == '__main__':
    matrix = [['F', 'A', 'C', 'I'],
             ['O', 'B', 'Q', 'P'],
             ['A', 'N', 'O', 'B'],
             ['M', 'A', 'S', 'S']]
    print(wordPresent(matrix, 'QP'))
