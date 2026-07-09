class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+","-","*","/"]
        for i in tokens:
            if(i in operators):
                s = int(stack.pop())
                f = int(stack.pop())
                if(i == "+"):
                    val = f+s
                elif (i == "-"):
                    val = f-s
                elif (i == "*"):
                    val = f*s
                else:
                    val = f/s
                stack.append(val)
            else:
                stack.append(i)
            print(stack)
        return int(stack.pop())

        
        