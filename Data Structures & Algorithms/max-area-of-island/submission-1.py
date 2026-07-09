class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])
        
        res = 0
        stack = []
        visited = set()
        
        for i in range(numRows):
            for j in range(numCols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    stack.append((i,j))
                    size = 0
                    while stack:
                        curr = stack.pop()
                        if curr not in visited:
                            visited.add((curr[0],curr[1]))
                            size +=1
                            for x,y in [(-1,0), (0,-1), (1,0), (0,1)]:
                                ix, jy = curr[0]+x, curr[1]+y
                                if ix>=0 and ix<numRows and jy>=0 and jy<numCols:
                                    if(grid[ix][jy] == 1):
                                        stack.append((ix,jy))
                    res = max(res, size)
        
        return res