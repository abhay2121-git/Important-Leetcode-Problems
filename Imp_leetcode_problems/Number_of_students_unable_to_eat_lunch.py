# Example 1:
# Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
# Output: 0

# Example 2:
# Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
# Output: 3

from typing import List
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = [0, 0]

        for s in students:
            count[s] += 1

        for sand in sandwiches:
            if count[sand] == 0:
                return count[0] + count[1]
            count[sand] -= 1
        
        return 0
    