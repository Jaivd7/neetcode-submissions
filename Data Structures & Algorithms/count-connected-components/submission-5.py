class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = []
        for i in range(n):
            parent.append(i)
        rank = [1] * n
        def find(node): #finds the parent node
            res = node

            while res != parent[res]: 
                # print("res is", res)
                # print("parent of res is", parent[res])
                parent[res] = parent[parent[res]] #reduces the steps with path compression
                res = parent[res]
            return res

        def union(node1, node2):
            p1, p2 = find(node1), find(node2)

            if p1 == p2: #If they have the same parent, part of the same SCC
                return 0
            
            if rank[p1] >= rank[p2]:
                parent[p2] = p1
                rank[p1] = rank[p1] + rank[p2]
            else:
                parent[p1] = p2
                rank[p2] = rank[p1]+rank[p2]
            return 1
        
        res = n #Start of with each component being individual
        for i,j in edges:
            # print(parent, rank)
            res = res - union(i,j) #if there is a union, there is one less strongly connected component
        return res