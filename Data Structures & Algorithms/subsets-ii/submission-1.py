class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        out = []
        curr = []
        def dfs(i):
            #Base Cases
            if i>=len(nums):
                out.append(curr[:]) #Shallow copy
                return 
            
            # Include
            curr.append(nums[i])
            dfs(i+1)
            curr.pop()

            # Do not include
            while i+1<len(nums) and nums[i+1] == nums[i]:
                i +=1
            dfs(i+1)
        dfs(0)
        return out