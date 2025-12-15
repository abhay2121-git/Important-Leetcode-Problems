# Maximun number of balloons
# Example 1:
# Input : text = "nlaebolko"
# Output : 1

# Example 2:
# Input : text = "loonbalxballpoon"
# Output : 2
from collections import defaultdict
class Solution:
    def __init__(self):
        pass

    def maxNumOfBalloons(self, text):
        counter = defaultdict(int)
        balloon = "balloon"

        for c in text:
            if c in balloon:
                counter[c] += 1

        if any(c not in counter for c in balloon):
            return 0
        else:
            return min(counter["b"], counter["a"], counter["l"]//2, counter["o"]//2, counter["n"])

text = "nlaebolko"
print(Solution().maxNumOfBalloons(text))