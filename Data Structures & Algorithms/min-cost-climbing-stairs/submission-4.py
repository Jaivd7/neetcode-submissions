class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        out = [0]*(len(cost)+1)
        for i in range(2, len(out)):
            out[i] = min(out[i-2]+cost[i-2], out[i-1]+cost[i-1])
        return out[-1]