class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num)) == 1:
            return num
        while len(str(num)) > 1:
            num = [int(i) for i in str(num)]
            num = sum(num)
        return num
