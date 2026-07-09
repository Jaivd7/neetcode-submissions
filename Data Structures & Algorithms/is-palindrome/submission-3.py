class Solution:

    def isPalindrome(self, s: str) -> bool:
        def isvalid(ch):
            o = ord(ch)
            return (ord('a') <= o <= ord('z') or
                    ord('A') <= o <= ord('Z') or
                    ord('0') <= o <= ord('9'))

        l, r = 0, len(s) - 1

        while l <= r:
            while l < r and not isvalid(s[l]):
                l += 1
            while r > l and not isvalid(s[r]):
                r -= 1

            if l > r:
                break

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
