# Example 1:
# Input: nums = [1,3,5,4,2,6]
# Output: true

# Example 2:
# Input: nums = [2,1,3]
# Output: false

from typing import List
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0

        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == 0:
            return False
        
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
        if i == 0 and i == n - 1:
            return False
        
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        return i == n - 1