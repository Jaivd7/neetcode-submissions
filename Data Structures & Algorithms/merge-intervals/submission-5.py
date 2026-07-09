class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            prev = res[-1]
            curr = intervals[i]

            if prev[1] < curr[0]: #Not overlapping
                res.append(curr)
            else:
                res.pop()
                out = [min(prev[0],curr[0]), max(prev[1], curr[1])]
                res.append(out)
        return res