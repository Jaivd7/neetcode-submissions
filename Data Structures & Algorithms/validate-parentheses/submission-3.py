class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {'}':'{', ']':'[', ')':'('}
        stack = []
        for i in s:
            if i not in hmap.keys():
                stack.append(i)
            else:
                #print(stack)
                if stack == []:
                    return False
                curr = stack.pop()
                if(hmap[i] != curr):
                    return False
        if stack == []:
            return True
        return False