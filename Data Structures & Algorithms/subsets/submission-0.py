class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if(len(nums) == 0):
            return []
        if len(nums) == 1:
            res = [[], nums]
            #print (res)
            return res
        else:
            prev = self.subsets(nums[1:len(nums)])
            res = []
            for i in prev:
                res.append(i)
                l = i.copy()
                l.append(nums[0])
                res.append(l)
            #print(res)
            return res