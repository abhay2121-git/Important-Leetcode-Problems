# Example 1:
# Input: mat = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]

# Example 2:
# Input: mat = [[1,2],[3,4]], r = 2, c = 4
# Output: [[1,2],[3,4]]

from typing import List
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        if m * n != r * c:
            return mat
        
        result = [[0] * c for _ in range(r)]

        for i in range(m):
            for j in range(n):
                idx = i * n + j
                result[idx // c][idx % c] = mat[i][j]
        
        return result
    
mat = [[1,2],[3,4]]
r = 1
c = 4
print(Solution().matrixReshape(mat, r, c))