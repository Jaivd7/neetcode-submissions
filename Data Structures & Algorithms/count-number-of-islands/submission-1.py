class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited = set()
        res = 0
        rows, cols = len(grid), len(grid[0])
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == "1" and (x, y) not in visited:
                    res += 1
                    stack = [(x, y)]
                    while stack:
                        cx, cy = stack.pop()
                        if (cx, cy) not in visited:
                            visited.add((cx, cy))
                            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                                nx, ny = cx + dx, cy + dy
                                if 0 <= nx < cols and 0 <= ny < rows and grid[ny][nx] == "1":
                                    stack.append((nx, ny))
        return res

