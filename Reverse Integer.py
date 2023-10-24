class Solution:
    def reverse(self, x: int) -> int:
        if not x:
            return 0

        x = list(str(x))[::-1]

        if x[-1] == "-":
            x.pop()
            x.insert(0,"-")
            
        x = int("".join(x))

        if x >= -2**31 and x <= 2**31:
            return x
        return 0
