class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = 0
        nums = ["1","2","3","4","5","6","7","8","9"]
        for i in s:
            if i in nums:
                length *= int(i)
            else:
                length += 1
        for j in s[::-1]:
            k %= length
            if k == 0 and j not in nums:
                return j
            if j in nums:
                length /= int(j)
            else:
                length -= 1
