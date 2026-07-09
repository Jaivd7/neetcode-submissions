class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0:
            return 0
        dp = [1,2]

        for i in range(n):
            if i>1:
                dp.append(dp[i-1]+dp[i-2])
        return dp[n-1]
