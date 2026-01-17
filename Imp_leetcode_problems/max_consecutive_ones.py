# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = curr = 0
        for n in nums:
            if n == 1:
                curr += 1
                max_count = max(max_count, curr)
            else:
                curr = 0
        return max_count
