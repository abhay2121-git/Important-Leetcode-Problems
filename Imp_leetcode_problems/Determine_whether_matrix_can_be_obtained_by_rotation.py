# Example 1:
# Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
# Output: true

# Example 2:
# Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
# Output: false

# Example 3:
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
# Output: true

from typing import List
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        for _ in range(4):
            if mat == target:
                return True
            
            for i in range(n):
                for j in range(i + 1, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

            for row in mat:
                row.reverse()

        return False
