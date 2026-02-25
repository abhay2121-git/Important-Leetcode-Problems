# Example 1:
# Input: nums = [3,2,1]
# Output: 1

# Example 2:
# Input: nums = [1,2]
# Output: 2

# Example 3:
# Input: nums = [2,2,3,1]
# Output: 1

from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float('-inf')

        for num in nums:
            if num == first or num == second or num == third:
                continue

            if num > first:
                third = second
                second = first
                first = num

            elif num > second:
                third = second
                second = num

            elif num > third:
                third = num

        return third if third != float('-inf') else first