class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        q = deque()
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        dist = 0
        while q:
            qLen = len(q)
            dist += 1
            for i in range(qLen):
                curr_x, curr_y = q.popleft()
                for x,y in [(1,0), (-1,0), (0,-1), (0,1)]:
                    xc, yc = curr_x + x, curr_y + y
                    if xc >= 0 and xc < rows and yc >= 0 and yc < cols:
                        if grid[xc][yc] == INF:
                            q.append((xc,yc))
                            grid[xc][yc] = dist
        
        return
        
