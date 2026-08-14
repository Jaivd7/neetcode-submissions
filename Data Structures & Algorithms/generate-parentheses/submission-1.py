class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        curr = []
        def dfs(open_b,  closed_b):
            # Base Case
            if open_b + closed_b == (2*n) - 1:
                curr.append(')')
                out.append(''.join(curr))
                curr.pop()
                return
            
            if open_b > closed_b:
                if open_b < n:
                    curr.append('(')
                    dfs(open_b +1, closed_b)
                    curr.pop()
                curr.append(')')
                dfs(open_b, closed_b+1)
                curr.pop()
            elif open_b == closed_b:
                curr.append('(')
                dfs(open_b +1, closed_b)
                curr.pop()
        dfs(0,0)

        return out