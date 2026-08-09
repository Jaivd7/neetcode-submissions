class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        low, high = max(weights), sum(weights)
        out = high
        while low <= high:
            mid = (low+high)//2
            remaining = mid
            count = 0
            for i in range(len(weights)):
                # print(mid, count, weights[i])
                if remaining - weights[i] >= 0:
                    remaining -= weights[i]
                else:
                    remaining = mid - weights[i]
                    count +=1
            count +=1
            if count <= days:
                out = mid
                high = mid - 1
            else:
                low = mid + 1
        return out
