# Example 1:
# Input: nums = [1,2,3,4,5]
# Output: true

# Example 2:
# Input: nums = [5,4,3,2,1]
# Output: false

# Example 3:
# Input: nums = [2,1,5,0,4,6]
# Output: true

from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False