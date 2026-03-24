# Example 1:
# Input: grid = [[1,2],[3,4]]
# Output: [[24,12],[8,6]]

# Example 2:
# Input: grid = [[12345],[2],[1]]
# Output: [[2],[0],[0]]

from typing import List
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n, m = len(grid), len(grid[0])
        total = n * m

        flat = [grid[i][j] for i in range(n) for j in range(m)]

        p = [1] * total

        prefix = 1
        for i in range(total):
            p[i] = prefix
            prefix = (prefix * flat[i]) % MOD

        suffix = 1
        for i in range(total - 1, -1, -1):
            p[i] = (p[i] * suffix) % MOD
            suffix = (suffix * flat[i]) % MOD

        return [[p[i * m + j] for j in range(m)] for i in range(n)]