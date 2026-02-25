# Example 1:
# Input: aliceSizes = [1,1], bobSizes = [2,2]
# Output: [1,2]

# Example 2:
# Input: aliceSizes = [1,2], bobSizes = [2,3]
# Output: [1,2]

# Example 3:
# Input: aliceSizes = [2], bobSizes = [1,3]
# Output: [2,3]

from typing import List
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        diff = (sumA - sumB) // 2

        bobSet = set(bobSizes)

        for x in aliceSizes:
            y = x - diff
            if y in bobSet:
                return [x, y]
