class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = 0
        b = x
        if(x < 0):
            return False
        while x != 0:
            a = (a*10) + x % 10
            x = x // 10
            
        if(a == b):
            return True
        return False
