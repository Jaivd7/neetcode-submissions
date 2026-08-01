class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        out = []
        for word in strs:
            key = [0] * 26
            for c in word:
                key[ord(c) - ord('a')] +=1
            key = tuple(key)
            if key in hmap:
                out[hmap[key]].append(word)
            else:
                out.append([word])
                hmap[key] = len(out) - 1
        return out
