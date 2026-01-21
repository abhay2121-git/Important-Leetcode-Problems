from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq = [0] * 101
        for num in nums:
            freq[num] += 1
    
        smaller = [0] * 101
        for i in range(1, 101):
            smaller[i] = smaller[i-1] + freq[i-1]
    
        return [smaller[num] for num in nums]