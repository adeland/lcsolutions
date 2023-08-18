class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 2
        if n == 1:
            return True
        if n == 2:
            return True
        else:
            pass
        while x != n:
            x *= 2
            if x > n:
                return False
            if x == n:
                return True
