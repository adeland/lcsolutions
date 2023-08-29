class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        from collections import Counter
        x = Counter(nums)
        x = [k for k, v in x.items() if v == 1]
        return x
