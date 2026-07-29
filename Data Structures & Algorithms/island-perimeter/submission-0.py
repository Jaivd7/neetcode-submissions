class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        stack = []
        visited = set()

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                
                if grid[x][y] == 1:
                    stack.append((x,y))
                    while stack:
                        xc,yc = stack.pop()
                        if (xc,yc) not in visited:
                            visited.add((xc,yc))
                            p = 0
                            for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
                                #Boundary
                                if xc+i >= len(grid) or xc+i <0 or yc+j >= len(grid[0]) or yc+j <0 or grid[xc+i][yc+j] == 0:
                                    p +=1
                                else: # Land
                                    stack.append((xc+i,yc+j))
                            perimeter += p
                    


        return perimeter