
class Solution:
    def __init__(self, sentence):
        self.sentence = sentence

    def circular_sentence(self):
        ss = sentence.split()
        n = len(ss)
        return (all(s[-1] == ss[(i + 1) % n][0] for i, s in enumerate(ss)))
sentence = "aabbccaa"
print(Solution(sentence).circular_sentence())

