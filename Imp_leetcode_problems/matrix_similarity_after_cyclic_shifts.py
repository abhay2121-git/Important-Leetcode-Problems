# Example 1:
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 4
# Output: false

# Example 2:
# Input: mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 2
# Output: true

# Example 3:
# Input: mat = [[2,2],[2,2]], k = 3
# Output: true

from typing import List
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        shift = k % n

        if shift == 0:
            return True

        for i, row in enumerate(mat):
            if i %2 == 0:
                shifted = row[shift:] + row[:shift]
            else:
                shifted = row[n - shift:] + row[:n - shift]

            if shifted != row:
                return False
            
        return True
