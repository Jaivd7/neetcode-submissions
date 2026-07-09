class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            if i == 0:
                prev = prices[0]
            else:
                diff = prices[i] - prev
                if(diff<0):
                    prev = prices[i]
                profit = max(profit, diff)
        return profit