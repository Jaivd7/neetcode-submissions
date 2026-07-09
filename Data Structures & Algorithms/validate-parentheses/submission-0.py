class Solution:
    def isValid(self, s: str) -> bool:
        brackets_open = ['{','[','(']
        brackets_closed = ['}',']',')']

        stack = []
        for i in s:
            print(i)
            if i in brackets_open:
                stack.append(i)
            else:
                if(len(stack) != 0):
                    index = brackets_closed.index(i)
                    if(stack[-1] == brackets_open[index]):
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        print(stack)
        if(len(stack) == 0):
            return True
        else:
            return False
        