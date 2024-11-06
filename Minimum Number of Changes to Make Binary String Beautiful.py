class Solution:
    def minChanges(self, s: str) -> int:
        
        ret = 0

        checks = [s[i:i+2] for i in range(0, len(s), 2)]

        for element in checks:
            if element[0] != element[1]:
                ret += 1
        
        return ret
