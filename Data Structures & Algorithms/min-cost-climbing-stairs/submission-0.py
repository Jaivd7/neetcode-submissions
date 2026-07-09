class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)<2:
            return 0
        l = [0]*(len(cost))
        l[0]=cost[0]
        l[1]=cost[1]
        for i in range(len(cost)):
            if i>1:
                l[i]=min(l[i-2],l[i-1]) + cost[i]
        return min(l[-1],l[-2])
        