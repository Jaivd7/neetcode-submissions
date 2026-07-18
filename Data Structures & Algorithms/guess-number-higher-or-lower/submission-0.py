# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, h = 1, n
        num = (l+h)//2
        curr = guess(num)
        while curr != 0:
            if curr == 1:
                l = num + 1
            else:
                h = num - 1
            num = (l+h)//2
            curr = guess(num)
        return num