class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        low, high = max(weights), sum(weights)
        out = high
        while low <= high:
            mid = (low+high)//2
            remaining = mid
            count = 1
            for i in range(len(weights)):
                if remaining - weights[i] < 0:
                    remaining = mid
                    count +=1
                remaining -= weights[i]
                    
            if count <= days:
                out = mid
                high = mid - 1
            else:
                low = mid + 1
        return out
