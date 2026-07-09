class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        length = len(nums)

        for i in range(length):
            if(target-nums[i]) in hmap:
                return [hmap[target-nums[i]],i]
            hmap[nums[i]] = i