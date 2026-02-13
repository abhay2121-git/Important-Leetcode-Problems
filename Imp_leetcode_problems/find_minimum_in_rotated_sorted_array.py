# Example 1:
# Input: nums = [3,4,5,1,2]
# Output: 1

# Example 2:
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0

# Example 3:
# Input: nums = [11,13,15,17]
# Output: 11

from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        if nums[left] < nums[right]:
            return nums[left]
        
        while left < right:
            mid = (left + right) >> 1

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]