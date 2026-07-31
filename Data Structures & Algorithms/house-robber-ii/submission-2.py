class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_line(houses):
            if len(houses) == 1:
                return houses[0]
            out = [houses[0], max(houses[0], houses[1])]
            for i in range(2, len(houses)):
                val = houses[i] + out[i-2]
                out.append(max(val, out[i-1]))
            return out[-1]

        # House 0 possibly included, last house excluded
        case1 = rob_line(nums[:-1])
        # House 0 excluded, last house possibly included
        case2 = rob_line(nums[1:])

        return max(case1, case2)