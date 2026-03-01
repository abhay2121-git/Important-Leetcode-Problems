# Example 1:
# Input: candyType = [1,1,2,2,3,3]
# Output: 3

# Example 2:
# Input: candyType = [1,1,2,3]
# Output: 2

# Example 3:
# Input: candyType = [6,6,6,6]
# Output: 1

from typing import List
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        unique_types = len(set(candyType))
        allowed = len(candyType) // 2

        return min(unique_types, allowed)
 