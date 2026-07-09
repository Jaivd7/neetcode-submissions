class Solution:
    def maxArea(self, heights: List[int]) -> int:
        nums = heights
        maxwater = 0
        l,r = 0, len(nums)-1

        while(l<r):
            vol = min(nums[l], nums[r]) * (r-l)
            maxwater = max(vol,maxwater)
            if(nums[l]>nums[r]):
                r-=1
            else:
                l+=1
        return maxwater
