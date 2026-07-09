class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0

        while i < len(nums):
            # If we can already reach or pass the end → success
            if i + nums[i] >= len(nums) - 1:
                return True

            best_reach = i  # farthest reachable index
            best_index = i  # index to jump to next

            # Explore all next positions reachable from i
            for step in range(1, nums[i] + 1):
                curr_i = i + step
                if curr_i >= len(nums):
                    break

                reach = curr_i + nums[curr_i]

                # Greedy choice: pick the index with the farthest reach
                if reach > best_reach:
                    best_reach = reach
                    best_index = curr_i

            # If we cannot move forward, we are stuck
            if best_index == i:
                return False

            # Jump to the next best position
            i = best_index

        return False

