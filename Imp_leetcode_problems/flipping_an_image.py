# Example 1:
# Input: image = [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]

# Example 2:
# Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

from typing import List
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            left = 0
            right = len(row) - 1

            while left <= right:
                if row[left] == row[right]:
                    row[left] ^= 1

                    if left != right:
                        row[right] ^= 1
                
                else:
                    pass

                left += 1
                right -= 1

        return image
