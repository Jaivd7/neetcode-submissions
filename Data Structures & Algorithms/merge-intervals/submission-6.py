class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])

        def isOverlapping(int1, int2):
            return int1[1] >= int2[0]
        out = [intervals[0]]
        for i in range(1, len(intervals)):
            left = out.pop()
            right = intervals[i]
            if isOverlapping(left, right):
                out.append([min(left[0],right[0]), max(left[1],right[1])])
            else:
                out.append(left)
                out.append(right)
        return out