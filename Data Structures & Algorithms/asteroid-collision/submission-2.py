class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            ast = asteroids[i]
            if ast > 0:
                stack.append(ast)
            elif stack and stack[-1] > 0:
                while stack:
                    curr = stack.pop()
                    if curr < 0:
                        stack.append(curr)
                        break
                    elif curr > abs(ast):
                        stack.append(curr)
                        break
                    elif curr < abs(ast):
                        continue
                    else:
                        break
                if not stack and curr != abs(ast):
                    stack.append(ast)
                elif curr < 0:
                    stack.append(ast)
            else:
                stack.append(ast)
        return stack