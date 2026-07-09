class Solution:
    def rob(self, nums: List[int]) -> int:
        out = []
        for i in range(len(nums)-1, -1, -1):
            print(out, i)
            if len(out)<2:
                out.append(nums[i])
            else:
                if(len(out) == 2):
                    #out.insert(0, nums[i]+out[1])
                    out.append(nums[i] + out[0])
                else:
                    #out.insert(0, nums[i]+max(out[1],out[2]))
                    out.append(nums[i] + max(out[len(out) -2], out[len(out) -3]))
        print(out)
        return max(out)
