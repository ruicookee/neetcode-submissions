class Solution:
    def mySqrt(self, x: int) -> int:
        n = 0
        while n*n <= x:
            if n*n == x:
                return n
            else:
                n += 1
        return n-1
            