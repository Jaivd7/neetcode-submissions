class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i_n1, i_n2 = m-1, n-1
        for i in range(len(nums1) - 1, -1, -1):
            if i_n1 >= 0 and i_n2 >= 0:
                if nums1[i_n1] >= nums2[i_n2]:
                    nums1[i] = nums1[i_n1]
                    i_n1 -= 1
                else:
                    nums1[i] = nums2[i_n2]
                    i_n2 -= 1
            elif i_n1 >= 0:
                nums1[i] = nums1[i_n1]
                i_n1 -= 1
            else:
                nums1[i] = nums2[i_n2]
                i_n2 -= 1