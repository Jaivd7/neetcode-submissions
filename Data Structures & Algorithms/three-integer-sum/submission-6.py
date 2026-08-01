class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        # [-4, -1, -1, 0, 1, 2]

        for i in range(len(nums)):
            if nums[i] > 0: #Can't pivot if the number is already greater than 0
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] +nums[r]
                if s == 0:
                    out.append([nums[i], nums[l], nums[r]])
                    l +=1
                    r -=1
                    while nums[l] == nums[l-1] and l<r:
                        l +=1
                elif s > 0:
                    r -=1
                else:
                    l +=1


        return out