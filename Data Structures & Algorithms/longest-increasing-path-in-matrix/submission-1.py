class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        numRows, numCols = len(matrix), len(matrix[0])
        path = [[-1]*numCols for _ in range(numRows)]

        def dfs(i,j, prev):
            if i<0 or i>=numRows or j<0 or j>=numCols or matrix[i][j] <= prev:
                return 0
            if path[i][j] != -1:
                return path[i][j]
            else:                   
                res = 1
                for x,y in [(-1,0), (1,0), (0,-1), (0,1)]:
                    dfsval = dfs(i+x,j+y, matrix[i][j])
                    res = max(res, 1 + dfsval)
                path[i][j] = res
                return res

        pathlen = 1
        for i in range(numRows):
            for j in range(numCols):
                pathlen = max(pathlen, dfs(i,j, -1))
        return pathlen