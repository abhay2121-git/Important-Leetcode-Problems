# Example 1:
# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]

# Example 2:
# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]

from typing import List
from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])

        for word in words[1:]:
            current = Counter(word)

            for char in common:
                common[char] = min(common[char], current[char])

        result = []

        for char in common:
            result.extend([char] * common[char])

        return result