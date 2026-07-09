class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l!=r:
            diff = target - numbers[l]
            #print(numbers[l], numbers[r], diff)
            if(numbers[r] == diff):
                return [l+1,r+1]
            elif (numbers[r] > diff):
                r -=1
            else:
                l +=1
        return [0]
