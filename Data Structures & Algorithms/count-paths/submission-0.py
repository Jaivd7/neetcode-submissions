class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize
        board_row = [0]*n
        board = [board_row]*m
        #print(board)
        numRows = m
        numCols = n

        for i in range(numCols):
            board[numRows-1][i] = 1
        for j in range(numRows):
            board[j][numCols-1] = 1
        
        for i in range(numRows-2, -1, -1):
            for j in range(numCols-2, -1, -1):
                # print(board[i+1][j], board[i][j+1])
                board[i][j] = board[i+1][j] + board[i][j+1]
        
        return board[0][0]