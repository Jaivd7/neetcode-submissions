class Solution:

    def isPalindrome(self, s: str) -> bool:
        def alphaNum(c):
            return (ord('A') <= ord(c) <= ord('Z') or 
                    ord('a') <= ord(c) <= ord('z') or 
                    ord('0') <= ord(c) <= ord('9'))
        #Python only solution
        #Time Complexity = O(n)
        #Space Complexity = O(n)

        s = s.lower()
        s2 = ''
        for i in s:
            if alphaNum(i):
                s2 += i
        return (s2 == s2[::-1])

        #Double pointer solution
        #Time Complexity = O(n)
        #Space Complexity = O(1)
        
        # s = s.lower()
        # r = len(s) - 1
        # l = 0
        # while (l<r):
        #     while l < r and not self.alphaNum(s[l]):
        #         l += 1
        #     while r > l and not self.alphaNum(s[r]):
        #         r -= 1
        #     if s[l] != s[r]:
        #         return False
        #     l += 1
        #     r = r - 1
        # return True


