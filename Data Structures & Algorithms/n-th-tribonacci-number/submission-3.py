class Solution:
    def tribonacci(self, n: int) -> int:
        one, two, three = 0, 1, 1
        if n < 1:
            return 0
        if n < 3:
            return 1
        
        for i in range(3, n+1):
            temp1 = three
            temp2 = two
            three = one + two + three
            two = temp1
            one = temp2
        return three