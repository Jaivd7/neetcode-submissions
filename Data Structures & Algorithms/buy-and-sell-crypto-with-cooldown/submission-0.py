class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        flag = True #False is sell, True is buy
        def dfs(index, flag):
            if index>=len(prices):
                return 0 
            if (index,flag) in dp:
                return dp[(index,flag)]
            
            #Buy
            if flag:
                buy = dfs(index+1, False) - prices[index]
                cooldown = dfs(index+1, True)
                dp[(index,flag)] = max(buy,cooldown)
            else: #Sell
                sell = dfs(index+2, True) + prices[index]
                cooldown = dfs(index+1, False)
                dp[(index,flag)] = max(sell,cooldown)
        
            return dp[(index, flag)]
            
        return dfs(0,flag)