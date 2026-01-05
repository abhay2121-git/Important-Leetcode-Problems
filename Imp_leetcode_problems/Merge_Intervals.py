# 56. Merge Intervals
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        merged = []
 
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
        
        return merged

# Another Approach
        # intervals.sort(key=lambda i: i[0])
        # output = [intervals[0]]

        # for start, end in intervals[1:]:
        #     lastEnd = output[-1][1]

        #     if start <= lastEnd:
        #         output[-1] = [output[-1][0], max(lastEnd, end)]
        #     else:
        #         output.append([start, end])
        # return output