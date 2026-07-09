class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        pos = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    pos.append((i,j))
        if len(pos) == 0:
            return 0
        visited = set()
        count = 0
        for i in pos:
            if(i not in visited):
                count +=1
                stack = [i]
                while stack:
                    curr = stack.pop()
                    visited.add(curr)
                    # up, down, left, right
                    directions = [(curr[0]+1,curr[1]),(curr[0]-1,curr[1]),(curr[0],curr[1]-1),(curr[0],curr[1]+1)]
                    for x,y in directions:
                        if((x,y) not in visited):
                            if(0<=x and x<len(grid) and 0<=y and y<(len(grid[0]))):
                                # print(x,y)
                                if(grid[x][y] == '1'):
                                    stack.append((x,y))


        return count
        


