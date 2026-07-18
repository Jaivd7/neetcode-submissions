class Solution:
    def mySqrt(self, x: int) -> int:
        l, h = 0, x
        prev = None
        mid = (l+h)//2
        while prev != mid:
            if mid * mid > x:
                h = mid -1
            else:
                prev = mid 
                l = mid +1
            mid = (l+h)//2
        return mid