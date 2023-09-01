class Solution:
    def arraySign(self, nums: List[int]) -> int:
        import math
        nums = int(math.prod(nums))
        if nums > 0:
            return 1
        if nums == 0:
            return 0
        else:
            return -1
