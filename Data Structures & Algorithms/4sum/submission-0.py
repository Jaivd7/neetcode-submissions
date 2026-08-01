class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        out = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: #Removing starting duplicates
                continue

            #Three sum
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]: # Removing duplicates for other numbers
                    continue

                l, r = j+1, len(nums)-1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s == target:
                        out.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s > target:
                        r -= 1
                    else:
                        l += 1

        return out