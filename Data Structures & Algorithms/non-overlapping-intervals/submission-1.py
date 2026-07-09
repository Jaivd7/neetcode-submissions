class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        remove = 0
        intervals.sort(key=lambda x: x[0])

        i = 0
        j = 1

        while j < len(intervals):
            prev = intervals[i]
            curr = intervals[j]

            if prev[1] <= curr[0]:  # no overlap (<= is standard)
                i = j              # move "kept" pointer forward
                j += 1
            else:
                remove += 1
                # overlap: keep the one that ends earlier
                if curr[1] < prev[1]:
                    i = j          # keep curr instead of prev
                j += 1

        return remove