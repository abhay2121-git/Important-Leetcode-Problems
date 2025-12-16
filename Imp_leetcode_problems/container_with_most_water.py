class Solution:
    def __init__(self, height):
        self.height = height
    
    def container(self):
        l, r = 0, len(height) - 1
        area = 0
        while l < r:
            area = max(area, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area

height = [1, 3, 5, 2, 8, 1, 6, 7]
print(Solution(height).container())

