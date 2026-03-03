# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:
# Input: numRows = 1
# Output: [[1]]

from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for i in range(1, numRows):
            prev = triangle[i - 1]
            row = [1]

            for j in range(1, i):
                row.append(prev[j - 1] + prev[j])
            
            row.append(1)
            triangle.append(row)

        return triangle
