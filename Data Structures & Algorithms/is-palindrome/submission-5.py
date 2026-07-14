class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphaNumeric(ch):
            if (ord('a') <= ord(ch) <= ord('z')) or (ord('A') <= ord(ch) <= ord('Z')) or (ord('0') <= ord(ch) <= ord('9')):
                return True
            return False
        s = s.lower()
        st, l = 0, len(s)-1
        while st <= l:
            if not isAlphaNumeric(s[st]):
                st +=1
            elif not isAlphaNumeric(s[l]):
                l -=1
            elif s[st] == s[l]:
                st +=1
                l -=1
            else:
                return False
        return True