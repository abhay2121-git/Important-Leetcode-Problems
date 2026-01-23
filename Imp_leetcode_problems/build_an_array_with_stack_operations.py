# Example 1:
# Input: target = [1,3], n = 3
# Output: ["Push","Push","Pop","Push"]

# Example 2:
# Input: target = [1,2,3], n = 3
# Output: ["Push","Push","Push"]

from typing import List
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        target_set = set(target)
        operations = []
        target_index = 0

        for current in range(1, n + 1):
            if current in target_set:
                operations.append("Push")
                target_index += 1

                if target_index == len(target):
                    break
            
            else:
                operations.append("Push")
                operations.append("Pop")
        
        return operations