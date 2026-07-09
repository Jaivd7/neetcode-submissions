class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        counts = []
        out = []
        for s in strs:
            flag = False
            hmap = {}
            for i in s:
                hmap[i] = 1 + hmap.get(i,0)
            for j in range(len(counts)):
                if hmap == counts[j]:
                    out[j].append(s)
                    flag = True
                    break
            if not flag:
                counts.append(hmap)
                out.append([s])
        return out
        