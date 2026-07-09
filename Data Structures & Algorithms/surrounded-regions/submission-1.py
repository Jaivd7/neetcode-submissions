class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS, COLS = len(board), len(board[0])

        def dfs(r,c):
            if board[r][c] == 'X' or board[r][c] == 'K':
                return
            if board[r][c] == 'O':
                board[r][c] = 'K'
                for x,y in [(-1,0),(1,0),(0,-1),(0,1)]:
                    if r+x < ROWS and r+x>=0 and c+y < COLS and c+y>=0:
                        dfs(r+x,c+y)
        

        for i in range(COLS):
            dfs(0,i)
            dfs(ROWS-1,i)
        
        for j in range(ROWS):
            dfs(j,0)
            dfs(j,COLS-1)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'K':
                    board[i][j] = 'O'
        return