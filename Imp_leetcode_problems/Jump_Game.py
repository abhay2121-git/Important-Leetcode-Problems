# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true

# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false

from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False

            max_reach = max(max_reach, i + nums[i])

            if max_reach >= len(nums) - 1:
                return True

        return True
