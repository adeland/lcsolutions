class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        z = Counter(nums)
        return (list(z.keys())[list(z.values()).index(1)])
