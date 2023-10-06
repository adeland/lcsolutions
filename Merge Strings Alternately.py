class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ret = []
        if len(word1) == len(word2):
            for i in range(len(word1)):
                ret.append(word1[i])
                ret.append(word2[i])
            ret = "".join(ret)
            return ret
        if len(word1) > len(word2):
            for i in range(len(word1)):
                if i == len(word2):
                    break
                ret.append(word1[i])
                ret.append(word2[i])
            ret.append(word1[i:])
            ret = "".join(ret)
            return ret
        else:
            for i in range(len(word2)):
                if i == len(word1):
                    break
                ret.append(word1[i])
                ret.append(word2[i])
            ret.append(word2[i:])
            ret = "".join(ret)
            return ret
