# Rotate Image
# Example:
# Input: matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# output : [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

class Solution:
    def __init__(self):
        pass

    def rotateimage(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
        return matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution().rotateimage(matrix))

