class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []

        def dfs(i, cur, total):
            #Base Case

            #Reached a match, append
            if total == target:
                self.res.append(cur.copy())
                return
            #Pruning totals that are not needed
            if i >= len(nums) or total > target:
                return

            #Repeat with current index
            cur.append(nums[i])
            dfs(i, cur, total + nums[i]) 
            cur.pop()
            #Move to the next index
            dfs(i + 1, cur, total) 

        dfs(0, [], 0)
        return self.res