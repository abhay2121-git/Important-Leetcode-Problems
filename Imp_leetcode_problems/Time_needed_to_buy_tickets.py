# Example 1:
# Input: tickets = [2,3,2], k = 2
# Output: 6

# Example 2:
# Input: tickets = [5,1,1,1], k = 0
# Output: 8

from typing import List
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0

        for i in range(len(tickets)):
            if i <= k:
                time += min(tickets[i], tickets[k])
            else:
                time += min(tickets[i], tickets[k] - 1)

        return time
    