class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        dic = Counter(nums)
        max1 = max(dic.values())
        x = list(dic.keys())
        y = list(dic.values())
        z = y.index(max1)
        return x[z]
