class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        def dfs(i, total):
            #Base Case

            #Reached a match, append
            if total == target:
                res.append(cur.copy())
                return
            #Pruning totals that are not needed
            if i >= len(nums) or total > target:
                return

            #Repeat with current index
            cur.append(nums[i])
            dfs(i, total + nums[i])
            cur.pop()
            #Move to the next index
            dfs(i + 1, total)

        dfs(0, 0)
        return res