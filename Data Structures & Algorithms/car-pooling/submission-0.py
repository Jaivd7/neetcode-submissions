class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key= lambda x:x[1])
        minheap = []
        total_pass = 0
        for trip in trips:
            p, start, end = trip
            while minheap and minheap[0][0] <= start:
                e, passengers = heapq.heappop(minheap)
                total_pass -= passengers
            
            total_pass +=p
            if total_pass > capacity:
                return False
            heapq.heappush(minheap, (end, p))
        return True