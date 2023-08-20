class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        import math
        if int(math.sqrt(num)) != math.sqrt(num):
            return False
        else:
            return True
