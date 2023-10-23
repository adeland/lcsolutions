class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0:
            return False
        if math.log2(n) % 2 == 0:
            return True
        return False
