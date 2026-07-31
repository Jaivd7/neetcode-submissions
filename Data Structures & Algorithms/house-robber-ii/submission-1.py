class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # House 0 included
        out = [nums[0]]
        for i in range(1, len(nums)):
            if i-2 >=0 and i!= len(nums)-1:
                val = nums[i] + out[i-2]
            elif i==len(nums)-1:
                 val = out[i-2]
            else:
                val = nums[i]
            out.append(max(val, out[i-1]))
        
        # House 0 not included
        out2 = [0]
        for i in range(1, len(nums)):
            if i-2 >=0:
                val = nums[i] + out2[i-2]
            else:
                val = nums[i]
            out2.append(max(val, out2[i-1]))
        return max(out[-1],out2[-1])
