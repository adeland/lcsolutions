class Solution:
    def partitionString(self, s: str) -> int:
        count = 0
        seen = []
        for i in s:
            if i not in seen:
                seen.append(i)
            elif i in seen:
                seen = []
                seen.append(i)
                count += 1
        return count + 1
