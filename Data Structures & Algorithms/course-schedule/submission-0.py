class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hmap = defaultdict(list)
        visited = set()

        for c,p in prerequisites:
            hmap[c].append(p)
        
        def dfs(course):
            if course in visited:
                return False
            if hmap[course] == []:
                return True
            visited.add(course)
            for i in hmap[course]:
                if not dfs(i):
                    return False
            visited.remove(course)
            hmap[course] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True