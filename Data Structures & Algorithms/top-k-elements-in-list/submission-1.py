class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = Counter(nums)
        sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
        print(sorted_dict)
        out = []
        for key, item in sorted_dict.items():
            if len(out) == k:
                break
            out.append(key)
        return out
        # nums.sort()
        # freq = [(nums[0],1)]
        # j = 0
        # for i in range(1,len(nums)):
        #     if(nums[i] == nums[i-1]):
        #         freq[j] += 1
        #     else:
        #         fre

