class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        numRows, numCols = len(grid), len(grid[0])
        q = deque()
        visited = set()
        fresh = set()

        def check(i,j):
            if (i<0 or i>=numRows or j<0 or j>=numCols or grid[i][j] !=1 or ((i,j) in visited)):
                return False
            else:
                q.append((i,j))
                visited.add((i,j))
                return True

        for i in range(numRows):
            for j in range(numCols):
                if grid[i][j] == 2:
                    q.append((i,j))
                    visited.add((i,j))
                elif grid[i][j] == 1:
                    fresh.add((i,j))
        
        res = 0
        while q:
            temp = False
            for i in range(len(q)):
                curri, currj = q.popleft()

                a = check(curri +1, currj)
                b = check(curri, currj +1)
                c = check(curri-1, currj)
                d = check(curri,currj-1)

                temp = a or b or c or d or temp
            if temp:
                res +=1
        for i in fresh:
            if i not in visited:
                return -1
        return res