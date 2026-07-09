class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        if nums == []:
            return res
        num = nums[0]
        max_num = target//num
        if(target%num == 0):
            res.append([num]*max_num) 
        for i in range(max_num):
            print(nums[1:], target-(num*i))
            out = self.combinationSum(nums[1:], target-(num*i))
            for j in out:
                curr = j.copy()
                curr.extend([num]*i)
                res.append(curr)
        return res