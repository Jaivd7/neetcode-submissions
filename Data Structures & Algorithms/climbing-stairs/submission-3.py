class Solution:
    def climbStairs(self, n: int) -> int:
        n1 = 1
        n2 = 2
        for i in range(2, n):
            curr = n1 + n2
            n1 = n2
            n2 = curr
        if n==1:
            return n1
        else:
            return n2
