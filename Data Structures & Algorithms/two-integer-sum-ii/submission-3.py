class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            diff = target - numbers[l]
            if numbers[r] == diff:
                break
            elif numbers[r] > diff:
                r -=1
            else:
                l +=1
        return [l+1, r+1]

        #[-4,-3,-2,-1] target -4