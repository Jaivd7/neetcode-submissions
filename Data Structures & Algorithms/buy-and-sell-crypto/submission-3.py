class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof = 0
        curr = prices[0]
        for i in range(len(prices)):
            if prices[i] < curr:
                curr = prices[i]
            if prices[i]-curr > maxprof:
                maxprof = prices[i] - curr
        return maxprof