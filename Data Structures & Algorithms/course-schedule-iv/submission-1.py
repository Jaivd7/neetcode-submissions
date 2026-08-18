class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = []
        prereq = {}
        for i in range(numCourses):
            adj_list.append([])
            prereq[i] = set()
        for course in prerequisites:
            adj_list[course[1]].append(course[0])
        
        def dfs(course):
            if prereq[course]:
                return prereq[course]
            
            for p in adj_list[course]:
                prereq[course].add(p)
                for pr in dfs(p):
                    prereq[course].add(pr)
            return prereq[course]
        
        for i in range(numCourses):
            dfs(i)
        
        out = []
        for p, c in queries:
            out.append(p in prereq[c])
        return out