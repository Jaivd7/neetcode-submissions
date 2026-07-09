class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def bc(openN, closedN, curr):
            if openN==closedN==n:
                res.append("".join(curr))
                return
            
            if openN < n:
                curr.append('(')
                bc(openN+1, closedN, curr)
                curr.pop()
            
            if closedN < openN:
                curr.append(')')
                bc(openN, closedN+1, curr)
                curr.pop()

        bc(0,0,[])
        return res