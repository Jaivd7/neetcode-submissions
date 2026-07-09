"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x:x.start)
        if len(intervals) == 0:
            return 0
        
        res = [intervals[0].end]
        days = 1
        for i in range(1,len(intervals)):
            curr = intervals[i]
            flag = False
            for j in range(len(res)):
                if res[j] <= curr.start:
                    flag = True
                    res[j] = curr.end
                    break
            if not flag:
                res.append(curr.end)
                days +=1
        return days