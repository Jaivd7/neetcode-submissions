class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i1, i2):
            temp = nums[i1]
            nums[i1] = nums[i2]
            nums[i2] = temp
        k = k % len(nums)
        if k == 0:
            return

        # Invert the whole array
        l, r = 0, len(nums) - 1
        while l<r:
            swap(l,r)
            l, r = l +1, r-1
        
        #Invert the two remaining segments
        l, r = 0, k-1
        while l<r:
            swap(l,r)
            l, r = l +1, r-1

        l, r = k, len(nums)-1
        while l<r:
            swap(l,r)
            l, r = l +1, r-1
        