class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ("+","-","*","/")
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in operations:
                s = stack.pop()
                f = stack.pop()
                if tokens[i] == "+":
                    stack.append(f+s)
                elif tokens[i] == "-":
                    stack.append(f-s)
                elif tokens[i] == "*":
                    stack.append(f*s)
                else:
                    stack.append(int(float(f/s)))
            else:
                stack.append(int(tokens[i]))
        return stack[-1]