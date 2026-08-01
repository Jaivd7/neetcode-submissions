class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_freq_num = 0
        max_freq = 0
        hmap = {}
        for i in nums:
            hmap[i] = hmap.get(i, 0) + 1
            if hmap[i] > max_freq:
                max_freq = hmap[i]
                max_freq_num = i
        print(hmap)
        return max_freq_num