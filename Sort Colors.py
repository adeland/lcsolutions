class Solution:
    def sortColors(self, nums: List[int]) -> None:
        a = nums.count(0)
        countA = 0
        b = nums.count(1)
        countB = 0
        c = nums.count(2)
        countC = 0
        if nums.count(0) >= 1:
            while a != countA:
                nums.append(0)
                countA += 1
                nums.remove(0)
        if nums.count(1) >= 1:
            while b != countB:
                nums.append(1)
                countB += 1
                nums.remove(1)
        if nums.count(2) >= 1:
            while c != countC:
                nums.append(2)
                countC += 1
                nums.remove(2)
