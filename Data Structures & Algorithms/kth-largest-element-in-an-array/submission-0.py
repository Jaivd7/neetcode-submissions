class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # sorting solution

        nums.sort()
        return nums[len(nums)-k]