from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2
    
nums = [1, 2, 3]
print(Solution().getConcatenation(nums))