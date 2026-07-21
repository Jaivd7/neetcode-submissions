class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minheap = []
        for val in stones:
            heapq.heappush(minheap, -val)
        while len(minheap) > 1 and minheap[0] != 0:
            l = -heapq.heappop(minheap)
            s = -heapq.heappop(minheap)
            heapq.heappush(minheap, -(l-s))
        return -minheap[0]