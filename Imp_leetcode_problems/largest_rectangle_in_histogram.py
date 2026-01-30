# Example 1:
# Input: heights = [2,1,5,6,2,3]
# Output: 10

# Example 2:
# Input: heights = [2,4]
# Output: 4

from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height_index = stack.pop()
                height = heights[height_index]

                width = i if not stack else i - stack[-1] - 1
                area = height * width
                max_area = max(max_area, area)
            
            stack.append(i)

        while stack:
            height_index = stack.pop()
            height = heights[height_index]
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            area = height * width
            max_area = max(max_area, area)
        
        return max_area