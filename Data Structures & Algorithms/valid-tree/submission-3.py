class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        hmap = {}
        for i in range(n):
            hmap[i] = []
        
        for edge in edges:
            hmap[edge[0]].append(edge[1])
            hmap[edge[1]].append(edge[0])
        visited = set()
        
        def dfs(i, parent):
            # print(parent, i)
            if i in visited:
                return False
            visited.add(i)
            for nei in hmap[i]:
                if nei != parent:
                    if not dfs(nei, i):
                        return False
            return True
        out = dfs(0, None)

        return out and len(visited)==n