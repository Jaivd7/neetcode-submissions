class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        for i in nums:
            if len(heap) < k:
                heapq.heappush(heap, i)
            else:
                if heap[0] < i:
                    heapq.heappop(heap)
                    heapq.heappush(heap, i)
        return heapq.heappop(heap)