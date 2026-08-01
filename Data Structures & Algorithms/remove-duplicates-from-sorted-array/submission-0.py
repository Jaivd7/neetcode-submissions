class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        l = 0
        for num in nums:
            if num not in seen:
                seen.add(num)
                nums[l] = num
                l +=1
        return l
