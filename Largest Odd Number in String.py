class Solution:
    def largestOddNumber(self, num: str) -> str:
        count = 0
        length = len(num)

        for element in num:
            count -= 1
            if int(num[count]) % 2 == 1:
              final = length + count
              return num[:final + 1]   
                   
        return ""
