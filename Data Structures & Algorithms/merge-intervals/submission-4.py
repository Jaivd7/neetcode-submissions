class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x:x[0])
        out = [intervals[0]]
        for i in range(1,len(intervals)):
            prev = out[-1]
            curr = intervals[i]
            if prev[1] >=  curr[0]:
                new = [min(prev[0],curr[0]), max(curr[1], prev[1])]
                out[-1] = new
            else:
                #out.append(prev)
                out.append(curr)
        return out