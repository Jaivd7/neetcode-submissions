class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dist(x1,x2):
            return ((x)**2 + (y)**2)**0.5
        
        minheap = []
        for x,y in points:
            heapq.heappush(minheap, (dist(x,y),[x,y]))
        out = []
        while minheap and len(out)<k:
            out.append(heapq.heappop(minheap)[1])
        return out