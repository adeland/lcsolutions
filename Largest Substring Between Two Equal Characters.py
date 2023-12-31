class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dic = {}
        ret = -1

        for index, char in enumerate(s):
            if char in dic:
                check = index - dic[char] - 1
                ret = max(ret, check)
            else:
                dic[char] = index
                
        return ret
