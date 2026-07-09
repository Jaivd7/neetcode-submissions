class Solution:
    def longestPalindrome(self, s: str) -> str:

        def isPalindrome(string):
            l, r = 0, len(string)-1
            while l<=r:
                if string[l] == string[r]:
                    l +=1
                    r -=1
                else:
                    return False
            return True

        for i in range(len(s), 0, -1):
            l = 0
            while(l+i <=len(s)):
                if isPalindrome(s[l:l+i]):
                    return s[l:l+i]
                else:
                    l +=1
        return ""
