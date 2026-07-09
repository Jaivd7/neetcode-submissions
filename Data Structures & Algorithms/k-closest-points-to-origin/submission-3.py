import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def dist(x1,y1):
            dist = math.sqrt((x1)**2 + (y1)**2)
            return dist

        distances = []
        for i,j in points:
            heapq.heappush(distances, (dist(i,j),i,j))
        
        out = []
        for i in range(k):
            val = heapq.heappop(distances)
            out.append([val[1], val[2]])
        
        return out