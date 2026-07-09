class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        largest = 0
        for y in range(rows):
            for x in range(cols):
                if((x,y) not in visited) and (grid[y][x] == 1):
                    stack = [(x,y)]
                    curr = 0
                    while stack:
                        cx, cy = stack.pop()
                        if((cx,cy) not in visited):
                            visited.add((cx,cy))
                            curr +=1
                            #print(curr,cy,cx)
                            for a,b in [(-1,0),(1,0),(0,-1),(0,1)]:
                                currx, curry = cx + a, cy + b
                                #print(curry, currx)

                                if 0<=currx<cols and 0<=curry<rows:
                                    if grid[curry][currx] == 1:
                                        stack.append((currx,curry))
                    largest = max(largest,curr)
        return largest

