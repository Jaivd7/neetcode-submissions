"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <2:
            return True
        sorted_intervals = sorted(intervals, key = lambda item:item.start)

        for i in range(1,len(sorted_intervals)):
            prev = sorted_intervals[i-1]
            nex = sorted_intervals[i]
            if(prev.end > nex.start):
                return False
        return True
