class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {'(':')', '{':'}', '[':']'}
        stack = []
        for i in range(len(s)):
            curr = s[i]
            if curr in hmap.keys():
                stack.append(curr)
            else:
                if not stack:
                    return False
                close = stack.pop()
                if hmap[close] != curr:
                    return False
        if stack:
            return False
        return True