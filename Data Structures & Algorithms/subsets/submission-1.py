class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = [[],[nums[0]]]
        for i in range(1,len(nums)):
            out2 = []
            for j in out:
                c = j +[nums[i]]
                out2.append(c)
            out = out + out2
        return out