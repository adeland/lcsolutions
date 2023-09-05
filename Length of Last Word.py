class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count1 = 0
        for i in s[::-1]:
            if i == " " and count1 == 0:
                continue
            if i != " ":
                count1 += 1
            if i == " " and count1 != 0:
                break
        return count1
            
            
            
