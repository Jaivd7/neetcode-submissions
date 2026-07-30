class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        out = [nums[0]]
        for i in range(1, len(nums)):
            if i-2 >=0:
                val = nums[i] + out[i-2]
            else:
                val = nums[i]
            out.append(max(val, out[i-1]))
        
        return out[-1]
