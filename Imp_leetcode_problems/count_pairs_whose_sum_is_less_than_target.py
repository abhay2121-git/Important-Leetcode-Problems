# Example 1:
# Input: nums = [-1,1,2,3,1], target = 2
# Output: 3

# Example 2:
# Input: nums = [-6,2,5,-2,-7,-1,3], target = -2
# Output: 10

from typing import List
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        
        while left < right:
            if nums[left] + nums[right] < target:
                count += right - left
                left += 1
            else:
                right -= 1
                
        return count
    