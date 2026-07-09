class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for i in range(n)]
        cols = set()
        pd = set() # r+c
        nd = set() # r-c
        res = []

        def backtrack(r):
            if r == n:
                copy = ["".join(i) for i in board]
                res.append(copy)
                return
            
            for c in range(n):
                if (c not in cols) and ((r-c) not in nd) and ((r+c) not in pd):
                    cols.add(c)
                    pd.add(r+c)
                    nd.add(r-c)
                    board[r][c] = "Q"

                    backtrack(r+1)

                    cols.remove(c)
                    pd.remove(r+c)
                    nd.remove(r-c)
                    board[r][c] = "."
        backtrack(0)
        return res

