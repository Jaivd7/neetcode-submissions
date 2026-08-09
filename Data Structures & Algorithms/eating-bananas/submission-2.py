class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        out = high
        while low <= high:
            k = (low+high)//2
            hours = 0
            for p in piles:
                hours += math.ceil(float(p) / k)
            if hours <= h: #Means our solution is valid
                out = k
                high = k - 1
            else:
                low = k + 1
        return out

            
