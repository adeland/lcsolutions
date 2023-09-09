class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        x = []
        i = 0
        while i < len(s):
            if s[i] not in x:
                x.append(s[i])
                i += 1
            else:
                longest = max(longest, len(x))
                x.pop(0)
        return max(longest, len(x))
