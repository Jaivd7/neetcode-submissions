class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # index
        l = r = 0

        while r < len(nums):
            #Remove values smaller than q from the q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            #Add the largest value 
            q.append(r)
            
            #if the new max is out of bounds, remove it 
            if l > q[0]:
                q.popleft()

            #  Once the window reaches size k, the front of the deque represents the maximum — add it to the output.
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output