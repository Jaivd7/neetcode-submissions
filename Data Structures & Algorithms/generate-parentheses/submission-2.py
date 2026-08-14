class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        curr = []
        def dfs(open_b,  closed_b):
            # Base Case
            if open_b == closed_b == n:
                out.append(''.join(curr))
                return
            
            if open_b < n:
                curr.append('(')
                dfs(open_b+1, closed_b)
                curr.pop()
            
            if closed_b < open_b:
                curr.append(')')
                dfs(open_b, closed_b+1)
                curr.pop()
        dfs(0,0)

        return out