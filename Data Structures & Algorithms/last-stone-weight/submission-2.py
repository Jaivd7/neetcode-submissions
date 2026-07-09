class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            if x > y:
                heapq.heappush(heap, y-x)
        
        heap.append(0)
        return abs(heap[0])