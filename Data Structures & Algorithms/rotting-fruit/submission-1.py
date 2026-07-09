class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        q = deque() #All Rotten Fruit
        fresh = 0
        visit = set()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                if grid[i][j] == 1:
                    fresh +=1
        
        time = 0
        
        while q:
            r,c,t = q.popleft()
            time = max(t,time)
            for x,y in ((-1,0),(1,0),(0,-1),(0,1)):
                rx, cy = r+x, c+y
                if 0 <= rx and rx < ROWS and 0 <= cy and cy < COLS and (rx,cy) not in visit:
                    if grid[rx][cy] == 1:
                        visit.add((rx,cy))
                        q.append((rx,cy,t+1))
                        fresh -=1
        return time if fresh ==0 else -1
        
                
