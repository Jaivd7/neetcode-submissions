class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        list = []
        for i in nums:
            if i in list:
                return True
            else:
                list.append(i)

        return False

        #Runtime O(n)
        #Space Complexity O(1)