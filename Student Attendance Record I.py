class Solution:
    def checkRecord(self, s: str) -> bool:
        a = 0
        l = 0
        for i in list(s):
            if i == "L":
                l += 1
            if l == 3:
                return False
            if i == "A":
                a += 1
                l = 0
            if i == "P":
                l = 0
        if a < 2:
            return True
        else:
            return False
