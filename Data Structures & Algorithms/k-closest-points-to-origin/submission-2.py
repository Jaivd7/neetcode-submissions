class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for i in points:
            heapq.heappush(minheap, [((i[0]**2)+(i[1]**2)), i[0], i[1]])
        
        res = []
        while len(res) != k:
            val = heapq.heappop(minheap)
            res.append([val[1], val[2]])
        
        return res
        