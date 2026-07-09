class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        def dfs(i):
            if i == len(nums)-1:
                return True
            if nums[i] == 0:
                return False
            
            for x in range(1,nums[i]+1):
                if dfs(i+x):
                    return True
            return False
        
        return dfs(0)