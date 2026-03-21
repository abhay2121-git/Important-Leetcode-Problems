# Example 1:
# Input: grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], x = 1, y = 0, k = 3
# Output: [[1,2,3,4],[13,14,15,8],[9,10,11,12],[5,6,7,16]]

# Example 2:
# Input: grid = [[3,4,2,3],[2,3,4,2]], x = 0, y = 2, k = 2
# Output: [[3,4,4,2],[2,3,2,3]]

from typing import List
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(k // 2):
            top_row = x + i
            bottom_row = x + (k - 1 - i)

            for j in range(y, y + k):
                grid[top_row][j], grid[bottom_row][j] = grid[bottom_row][j], grid[top_row][j]
        
        return grid
        