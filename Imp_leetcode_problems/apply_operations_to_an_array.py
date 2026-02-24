# Example 1:
# Input: nums = [1,2,2,1,1,0]
# Output: [1,4,2,0,0,0]

# Example 2:
# Input: nums = [0,1]
# Output: [1,0]

from typing import List
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        pos = 0
        for i in range(n):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1

        return nums
