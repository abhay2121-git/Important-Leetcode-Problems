# Example 1:
# Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
# Output: 1

# Example 2:
# Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3

from typing import List
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        row_sum = [sum(mat[i]) for i in range(m)]
        col_sum = [sum(mat[i][j] for i in range(m)) for j in range(n)]

        count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1:
                    count += 1

        return count
