class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {'}':'{', ')':'(', ']':'['}
        stack = []
        for i in s:
            # print(stack)
            if i in hmap.keys():
                if not stack:
                    return False
                curr = stack.pop()
                if hmap[i] != curr:
                    return False
            else:
                stack.append(i)
        # print("Final", stack)
        if not stack:
            return True
        return False