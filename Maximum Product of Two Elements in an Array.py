class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        vals = []
        
        for i, j in enumerate(nums):
            vals.append([j,i])
        vals = sorted(vals)
        l, r = vals[-1][0] - 1, vals[-2][0] -1
        
        return l * r

