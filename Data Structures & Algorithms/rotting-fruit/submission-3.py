class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        time = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh +=1
                if grid[i][j] == 2:
                    q.append((i,j))
        
        while q and fresh:
            qLen = len(q)
            time +=1
            for i in range(qLen):
                curr_x, curr_y = q.popleft()
                for (x,y) in [(1,0), (0,1), (-1,0), (0,-1)]:
                    cx, cy = curr_x + x, curr_y + y
                    if cx >= 0 and cx < rows and cy >=0 and cy < cols:
                        if grid[cx][cy] == 1:
                            grid[cx][cy] = 2 #Mutating the grid to mark what we have seen
                            fresh -=1
                            q.append((cx,cy))
        if fresh > 0:
            return -1
        return time
        