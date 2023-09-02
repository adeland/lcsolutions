class Solution:
    def isPalindrome(self, s: str) -> bool:
        nums = ("0","1","2","3","4","5","6","7","8","9")
        z = []
        s = list(s.lower())
        for i in s:
            if i in string.ascii_lowercase or i in nums:
                z.append(i)
        if z == z[::-1]:
            return True
        return False
