class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        res = nums[0]

        for num in nums:
            cur = max(num, cur + num)
            res = max(res, cur)

        return res