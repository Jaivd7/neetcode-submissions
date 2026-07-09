class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        visited = set()
        count = 0
        stack = []
        for i in range(n):
            if i not in visited:
                count +=1
                stack.append(i)
                while stack:
                    curr = stack.pop()
                    if curr in visited:
                        continue
                    else:
                        visited.add(curr)
                        for x in adj[curr]:
                            stack.append(x)
        return count
