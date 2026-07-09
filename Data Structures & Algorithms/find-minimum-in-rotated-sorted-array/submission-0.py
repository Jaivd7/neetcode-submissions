class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1

        while(low<high):
            mid = (low+high)//2
            if(mid==low or mid==high):
                break
            if nums[mid] > nums[len(nums)-1]:
                low = mid
            else:
                high = mid
        return min(nums[low], nums[high])