class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            curr = nums[i]
            if (target-curr) in hmap:
                return [hmap[target-curr], i]
            else:
                hmap[curr] = i