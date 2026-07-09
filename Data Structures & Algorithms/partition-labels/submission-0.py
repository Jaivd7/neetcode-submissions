class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hmap = {} #Stores all the last indexes

        for i in range(len(s)):
            hmap[s[i]] = i

        res = []
        farthest_reach = 0
        end = 0
        for i in range(len(s)):
            print(farthest_reach, end, res)
            c = s[i]
            if hmap[c] == i and i == farthest_reach: #Reached the Max
                res.append(farthest_reach - end + 1)
                end = farthest_reach +1 
                farthest_reach += 1
            else:
                farthest_reach = max(hmap[c], farthest_reach)
        return res