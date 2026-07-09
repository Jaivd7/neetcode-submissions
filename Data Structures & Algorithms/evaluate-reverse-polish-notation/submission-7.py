class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ('+','-','*','/')
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in operations:
                nex = stack.pop()
                prev = stack.pop()
                if tokens[i] == '+':
                    result = prev + nex
                elif tokens[i] == '-':
                    result = prev - nex
                elif tokens[i] == '*':
                    result = prev * nex
                else:
                    result = prev / nex
                stack.append(int(result))
            else:
                stack.append(int(tokens[i]))
        return (stack.pop())
        