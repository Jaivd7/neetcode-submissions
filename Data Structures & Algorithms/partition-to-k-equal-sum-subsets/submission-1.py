class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        max_subset = sum(nums) // k
        subsets = [0] * k

        nums.sort(reverse = True)
        def dfs(i):
            # Base Case
            if i == len(nums):
                return True
            
            for j in range(len(subsets)):
                if subsets[j] + nums[i] <= max_subset:
                    subsets[j] += nums[i]
                    if dfs(i+1):
                        return True
                    subsets[j] -= nums[i]
                if subsets[j] == 0: # No need to check other empty buckets because this is already empty
                    break
            
            return False
        return dfs(0)
