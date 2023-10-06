class Solution:
    def integerBreak(self, n: int) -> int:
        count3 = 0
        count2 = 0
        ret = 1
        if n == 2:
           return 1
        if n == 3:
            return 2
        while n != 0:
            if n == 4:
                count2 += 2
                break
            if n == 2:
                count2 += 1
                break
            n -= 3
            count3 += 1
        while count3 != 0:
            ret *= 3
            count3 -= 1
        while count2 != 0:
            ret *= 2
            count2 -= 1
        return ret
