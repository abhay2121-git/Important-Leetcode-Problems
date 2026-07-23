# Example 1:
# Input: nums = [1,2,2,4]
# Output: [2,3]

# Example 2:
# Input: nums = [1,1]
# Output: [1,2]

from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        unique_sum = sum(set(nums))

        duplicate = actual_sum - unique_sum
        missing = expected_sum - unique_sum

        return [duplicate, missing]

if __name__ == "__main__":
    nums = [1,2,2,4]
    sol = Solution().findErrorNums(nums)
    print(sol)