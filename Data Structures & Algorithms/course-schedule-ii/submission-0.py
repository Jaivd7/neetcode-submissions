class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hmap = defaultdict(list)
        cycle = set()
        visited = set()
        out = []

        for c,p in prerequisites:
            hmap[c].append(p)
        
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            for i in hmap[course]:
                if not dfs(i):
                    return False
            cycle.remove(course)
            visited.add(course)
            hmap[course] = []
            out.append(course)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return out