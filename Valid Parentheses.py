class Solution:
    def isValid(self, s: str) -> bool:
        dic  = {")": "(", "]": "[", "}": "{"}
        x = []
        for i in s:
            if i not in dic:
                x.append(i)
                continue
            if not x or x[-1] != dic[i]:
                return False
            x.pop()

        return not x
