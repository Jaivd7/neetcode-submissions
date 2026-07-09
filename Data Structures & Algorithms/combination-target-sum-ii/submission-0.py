class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def dfs(i, cur, total):
            print(cur)
            if total == 0:
                res.append(cur.copy())
                return 
            if total < 0 or i >=len(candidates):
                return

            cur.append(candidates[i])     
            #Including the current
            dfs(i+1, cur, total-candidates[i])

            cur.pop()
            #Not including the current candidate
            while i+1<len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, cur, total)
        dfs(0, [], target)
        return res