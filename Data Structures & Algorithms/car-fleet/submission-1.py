class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        com = []
        for i in range(len(position)):
            com.append((position[i],speed[i]))
        com.sort(key=lambda x: x[0], reverse = True)
        
        stack = []
        for i in com:
            time = (target - i[0])/i[1]
            if not stack:
                stack.append(time)
            else:
                if time>stack[-1]:
                    stack.append(time)
        return len(stack)