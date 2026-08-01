# Example 1:
# Input: nums = [1,1,2,2,3,4]
# Output: true

# Example 2:
# Input: nums = [1,1,1,1]
# Output: false

from collections import Counter
from typing import List
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter = Counter(nums)

        for f in counter.values():
            if f > 2:
                return False
        return True

if __name__ == "__main__":
    nums = [1,1,2,2,3,4]
    sol = Solution().isPossibleToSplit(nums)
    print(sol)
    