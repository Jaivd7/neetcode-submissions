class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = []
        for i in range(0, n+1):
            par.append(i)
        rank = [1]*(n+1)

        def find(node):
            curr = node

            while curr != par[curr]:
                par[curr] = par[par[curr]]
                curr = par[curr]
            return curr

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1==p2:
                return [n1,n2]
            
            if rank[p1]>=rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return [0,0]
        
        for i,j in edges:
            if union(i,j)[0] != 0:
                return [i,j]