class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = []
        heapq.heapify(n)
        for i in nums:
            heapq.heappush(n, -i)
        for i in range(k):
            if i == k-1:
                return -heapq.heappop(n)
            heapq.heappop(n)