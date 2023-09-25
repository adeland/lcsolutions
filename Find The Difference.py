class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(t) == 1:
            return t
        t = list(t)
        for i in s:
            if i in t:
                t.remove(i)
        return t[0]
