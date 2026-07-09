class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hmap = {}
        for i in range(len(s)):
            hmap[s[i]] = hmap.get(s[i], 0) + 1
        
        for i in range(len(t)):
            if t[i] not in hmap.keys():
                return False
            hmap[t[i]] -=1
        for key, value in hmap.items():
            if value != 0:
                return False
        return True
