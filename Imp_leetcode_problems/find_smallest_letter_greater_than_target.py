# Example 1:
# Input: letters = ["c","f","j"], target = "a"
# Output: "c"

# Example 2:
# Input: letters = ["c","f","j"], target = "c"
# Output: "f"

# Example 3:
# Input: letters = ["x","x","y","y"], target = "z"
# Output: "x"

from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters) - 1

        if target >= letters[-1]:
            return letters[0]
        
        while l < r:
            mid = l + (r - l) // 2

            if letters[mid] > target:
                r = mid
            else:
                l = mid + 1
        
        return letters[l]