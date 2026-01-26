# Example 1:
# Input: arr = [4,2,1,3]
# Output: [[1,2],[2,3],[3,4]]

# Example 2:
# Input: arr = [1,3,6,10,15]
# Output: [[1,3]]

from typing import List
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result = []

        min_diff = float('inf')
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            
            if diff < min_diff:
                min_diff = diff
                result = [[arr[i], arr[i + 1]]]
            
            elif diff == min_diff:
                result.append([arr[i], arr[i + 1]])

        return result