class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ['+','-','*','/']
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in operations:
                #print(tokens[i])
                b = stack.pop()
                a = stack.pop()
                if tokens[i] == '+':
                    result = a + b
                    #print(result)
                elif tokens[i] == '-':
                    result = a - b
                elif tokens[i] == '*':
                    result = a * b
                elif tokens[i] == '/':
                    result = int(a / b)
                stack.append(result)
            else:
                stack.append(int(tokens[i]))
        return stack.pop()

        
        