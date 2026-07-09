class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []

        def dfs(i, cur, total):
            if total == target:
                self.res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return

            cur.append(nums[i])
            dfs(i, cur, total + nums[i]) # all the copies with the multiples
            cur.pop()
            dfs(i + 1, cur, total) #next index

        dfs(0, [], 0)
        return self.res