class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = []
        heapq.heapify(s)
        for i in stones:
            heapq.heappush(s, -i)
        
        while(len(s)>1):
            f = -(heapq.heappop(s))
            se = -(heapq.heappop(s))
            res = -(f-se)
            heapq.heappush(s,res)
        
        return -heapq.heappop(s)