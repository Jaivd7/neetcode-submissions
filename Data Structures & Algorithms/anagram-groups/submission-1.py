class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        out_sets = []
        for i in strs:
            curr = Counter(i)
            if (curr in out_sets):
                index = out_sets.index(curr)
                out[index].append(i)
            else:
                out_sets.append(curr)
                out.append([i])
            print(out, out_sets)
        return out

        