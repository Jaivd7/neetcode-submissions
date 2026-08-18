class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent, rank = [0], [0]
        n = len(edges)
        for i in range(1, n+1):
            parent.append(i)
            rank.append(1)

        def find(node): #returns the parent of the node
            res = node
            while res != parent[res]:
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
        
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)

            if p1 == p2:
                return 0 #Already connected
            
            if rank[p1] >= rank[p2]:
                print("Here")
                rank[p1] += rank[p2]
                parent[p2] = p1
            else:
                rank[p2] += rank[p1]
                parent[p1] = p2
            return 1

        out = []
        for edge in edges:
            res = union(edge[0], edge[1])
            if res == 0:
                out = edge
        return out