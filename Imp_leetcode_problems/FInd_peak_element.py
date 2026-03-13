# Example 1:
# Input: nums = [1,2,3,1]
# Output: 2

# Example 2:
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5

from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) >> 1

            if nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid
        
        return low
    
    