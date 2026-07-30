class Solution:
    def tribonacci(self, n: int) -> int:

        fib = [0,1,1]

        if n < 3:
            return fib[n]

        for i in range(n+1):
            if (i-3) >= 0:
                fib.append(fib[i-3] + fib[i-2] +fib[i-1])
        return fib[-1]