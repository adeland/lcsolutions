class Solution:  
    import math
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        start, end, n = 1, 1, len(nums)
        out = [1]*n 
        for i in range(n):
            out[i] *= start
            start *= nums[i]
            out[~i] *= end
            end *= nums[~i]
        return out
