class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = cost[0], cost[1]

        for i in range(2, len(cost)):
            temp = min(one, two) + cost[i]
            one = two
            two = temp
        return min(one,two)