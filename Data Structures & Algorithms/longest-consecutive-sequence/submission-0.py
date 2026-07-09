class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Brute Force is sort it and then do max
        # Time is O(nlogn) space is O(1)
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

        