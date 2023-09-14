class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        t = list(t)
        for i in s:
            if i in t:
                z = t.index(i)
                t = t[z+1:]
            else:
                return False
        return True
