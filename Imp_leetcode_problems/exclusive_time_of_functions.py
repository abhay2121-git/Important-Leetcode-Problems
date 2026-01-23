# Example 1:
# Input: n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
# Output: [3,4]

from typing import List
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fn_id, action, time = log.split(":")
            fn_id = int(fn_id)
            time = int(time)

            if action == "start":
                if stack:
                    result[stack[-1]] += time - prev_time
                stack.append(fn_id)

                prev_time = time

            else:
                finished_fn = stack.pop()
                result[finished_fn] += time - prev_time + 1

                prev_time = time + 1
        
        return result