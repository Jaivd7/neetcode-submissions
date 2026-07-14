class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = 0
        w2 = 0
        s = ""
        while w1 < len(word1) or w2 < len(word2):
            if w1 == len(word1):
                return s+word2[w2:]
            if w2 == len(word2):
                return s+word1[w1:]
            s = s + word1[w1] + word2[w2]
            w1 += 1
            w2 += 1
        return s