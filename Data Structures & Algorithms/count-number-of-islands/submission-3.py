class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if (x,y) not in visited and grid[x][y] == '1':
                    stack = []
                    stack.append((x,y))
                    islands +=1
                    while stack:
                        xa, ya = stack.pop()
                        if (xa,ya) not in visited:
                            visited.add((xa,ya))
                            for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
                                xc, yc = xa+i, ya+j
                                if xc >= 0 and xc < len(grid) and yc >= 0 and yc < len(grid[0]) and grid[xc][yc] == '1':
                                    stack.append((xc,yc))


        return islands