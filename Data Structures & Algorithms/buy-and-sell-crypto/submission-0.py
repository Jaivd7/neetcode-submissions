class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        curr = prices[0]
        for i in range(len(prices)):
            if((prices[i]-curr)>max_prof):
                max_prof = prices[i]-curr
            if(prices[i]<curr):
                curr = prices[i]
        return max_prof

        