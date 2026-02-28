# Example 1:
# Input: g = [1,2,3], s = [1,1]
# Output: 1

# Example 2:
# Input: g = [1,2], s = [1,2,3]
# Output: 2

from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()

        child = 0
        cookie = 0

        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1

            cookie += 1

        return child
