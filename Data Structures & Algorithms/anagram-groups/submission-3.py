class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for i in range(len(strs)):
            s = strs[i]
            curr = [0] * 26
            for j in s:
                curr[ord(j)-ord("a")] += 1
            hmap[str(curr)].append(s)
        return list(hmap.values())
            