class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        numRows = len(board)
        numCols = len(board[0])

        def dfs(i,j,letter):
            if i<0 or i>=numRows:
                return False
            if j<0 or j>=numCols:
                return False
            if board[i][j] != word[letter]:
                return False
            if letter == (len(word)-1):
                return True
            # mark visited
            temp = board[i][j]
            board[i][j] = "#"
            
            found = (dfs(i-1,j,letter+1) or dfs(i,j-1,letter+1) or dfs(i+1,j,letter+1) or dfs(i,j+1,letter+1))

            board[i][j] = temp

            return found

        for i in range(numRows):
            for j in range(numCols):
                if dfs(i,j,0):
                    return True
        return False