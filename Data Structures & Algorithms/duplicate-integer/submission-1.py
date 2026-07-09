class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        #Runtime O(n^2)
        #Space Complexity O(n)         
        # list = []
        # for i in nums:
        #     if i in list:
        #         return True
        #     else:
        #         list.append(i)

        # return False

        # Time Complexity O(n)
        # Space Complexity O(n)
        set1 = set(nums)
        if len(set1) == len(nums):
            return False
        else:
            return True

