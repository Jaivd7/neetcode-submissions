# 1 1 1 1
# 1 11 1
# 1 1 11
# 11 1 1
# 11 11

class Solution:
    def numDecodings(self, s: str) -> int:

        def dp(s):
            if len(s) == 0:
                return 1
            if s[0] == '0':
                return 0
            if len(s) == 1:
                return 1
            
            if int(s[0:2]) <= 26:
                res = dp(s[1:]) + dp(s[2:])
            else:
                res = dp(s[1:])
            return res
        
        return dp(s)

