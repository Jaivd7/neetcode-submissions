class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        rows, cols = len(heights), len(heights[0])
        
        def dfs(curr_x, curr_y, visited, prevHeight):
            visited.add((curr_x, curr_y))
            for x,y in [(1,0), (0,1), (-1,0), (0,-1)]:
                cx, cy = curr_x + x, curr_y + y
                if cx >= 0 and cx < rows and cy >= 0 and cy < cols:
                    if (cx,cy) not in visited and heights[cx][cy] >= prevHeight:
                        dfs(cx,cy,visited,heights[cx][cy])
            

        for i in range(rows):
            dfs(i,0,pacific, heights[i][0])
            dfs(i, cols-1, atlantic, heights[i][cols-1])
        for j in range(cols):
            dfs(0,j,pacific, heights[0][j])
            dfs(rows-1, j, atlantic, heights[rows-1][j])

        out = []
        for i in range(rows):
            for j in range(cols):
                if (i,j) in pacific and (i,j) in atlantic:
                    out.append([i,j])

        return out