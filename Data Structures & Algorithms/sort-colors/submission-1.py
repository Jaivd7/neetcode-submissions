class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Counting Sort
        # hmap = {0:0, 1:0, 2:0}
        # for num in nums:
        #     hmap[num] = hmap[num] + 1
        # color = 0
        # i = 0
        # while i < len(nums):
        #     if hmap[color] > 0:
        #         nums[i] = color
        #         hmap[color] -= 1
        #         i +=1
        #     else:
        #         color +=1

        l, r = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        #Basically sotring all 0s at the begining, 2s at the end and then ones after the zeros and just keeping track of the boundaries
        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1
        