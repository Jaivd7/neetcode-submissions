class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        s = s.lower()
        
        def isvalid(s):
            if ord('A') <= ord(s) <= ord('Z') or ord('a') <= ord(s) <= ord('z') or ord('0') <= ord(s) <= ord('9'):
                return True
            return False

        while l<r:
            if isvalid(s[l]) and isvalid(s[r]):
                if s[l] == s[r]:
                    l +=1
                    r -=1
                else:
                    return False
            else:
                if isvalid(s[l]):
                    r -=1
                else:
                    l +=1
        return True
