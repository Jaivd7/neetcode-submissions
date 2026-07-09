class Solution:
    def climbStairs(self, n: int) -> int:
        out = [1,2]
        # if n<=len(out):
        #     return out[n-1]
        
        for i in range(2,n):
            s1 = out[i-1]
            s2 = out[i-2] 
            out.append(s1+s2)
        
        return out[n-1]
