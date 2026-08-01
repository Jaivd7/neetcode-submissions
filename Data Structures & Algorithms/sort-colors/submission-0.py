class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Counting Sort
        hmap = {0:0, 1:0, 2:0}
        for num in nums:
            hmap[num] = hmap[num] + 1
        color = 0
        i = 0
        while i < len(nums):
            if hmap[color] > 0:
                nums[i] = color
                hmap[color] -= 1
                i +=1
            else:
                color +=1
        