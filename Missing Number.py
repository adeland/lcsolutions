class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = list(range(len(nums) + 1))
        for i in nums:
            if i in x:
                x.remove(i)
        return x[0]
