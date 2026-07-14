class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hmap = {}
        for i in range(len(nums)):
            if nums[i] in hmap.keys():
                if abs(hmap[nums[i]]-i) <=k:
                    return True
                hmap[nums[i]] = i
            else:
                hmap[nums[i]] = i
        return False