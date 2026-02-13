# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# Example 3:
# Input: nums = [1,0,1,2]
# Output: 3

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        longest = 0

        for num in hash_set:
            if num - 1 not in hash_set:
                current = num
                length = 1

                while current + 1 in hash_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest