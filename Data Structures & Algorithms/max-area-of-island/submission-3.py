from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        q = deque()
        out = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1 and (x,y) not in visited:
                    q.append((x,y))
                    cur = 1
                    visited.add((x,y))
                    while q:
                        xa, ya = q.popleft()
                        for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
                            xc, yc = xa + i, ya + j
                            if xc>=0 and xc<len(grid) and yc>=0 and yc<len(grid[0]) and grid[xc][yc] == 1:
                                if (xc,yc) not in visited:
                                    visited.add((xc,yc))
                                    q.append((xc,yc))
                                    cur +=1
                    out = max(out,cur)
                        
        return out