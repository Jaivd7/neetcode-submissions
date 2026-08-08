class Solution:
    def decodeString(self, s: str) -> str:
    
        stack = []

        for c in s:
            if c == '[':
                stack.append(c) 
            elif c == ']':
                string = ""
                while stack[-1] != '[':
                    # print(stack)
                    char = stack.pop()
                    string = char + string
                stack.pop()
                multiple = stack.pop()
                string2 = ""
                for i in range(int(multiple)):
                    string2 += string
                stack.append(string2)
            elif c.isdigit():
                if stack and stack[-1].isdigit():
                    curr = stack.pop()
                    curr += c
                    stack.append(curr)
                else:
                    stack.append(c)
            else:
                stack.append(c)
        out = ""
        for string in stack:
            out += string
        return out