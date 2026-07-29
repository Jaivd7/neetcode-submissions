class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        out = []
        subset = []

        def dfs(i, t):
            #Base Case
            #Reached a solution
            if t == 0:
                out.append(subset.copy())
                return
            #Pruning numbers too large
            if i >= len(nums) or nums[i] > t:
                return
            
            #Include
            subset.append(nums[i])
            dfs(i+1, t-nums[i])
            subset.pop()

            #Do not include
            while i+1<len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1,t)
        
        dfs(0, target)
        return out