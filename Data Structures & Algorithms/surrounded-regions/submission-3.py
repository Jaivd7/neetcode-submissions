class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        visited = set()
        rows, cols = len(board), len(board[0])

        def dfs(i,j):
            # print(board[i][j])
            stack = []
            if board[i][j] == 'O':
                stack.append((i,j))
                while stack:
                    # print(stack)
                    curr_x, curr_y = stack.pop()
                    if (curr_x, curr_y) not in visited:
                        visited.add((curr_x, curr_y))
                        for x,y in [(1,0), (0,1), (-1,0), (0,-1)]:
                            cx, cy = curr_x + x, curr_y + y
                            if cx >=0 and cx < rows and cy >=0 and cy < cols:
                                if board[cx][cy] == 'O':
                                    stack.append((cx, cy))
                                

        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols-1)
        
        for j in range(cols):
            dfs(0,j)
            dfs(rows-1, j)
        # print(visited)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and (i,j) not in visited:
                    board[i][j] = 'X'