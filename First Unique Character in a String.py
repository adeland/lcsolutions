class Solution:
    def firstUniqChar(self, s: str) -> int:
        occur = Counter(s)
        for element in occur:
            if occur.get(element) < 2:
                return s.index(element)
        return -1
