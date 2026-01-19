# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]

# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]

from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits

digits =  [1,2,3]
print(Solution().plusOne(digits))