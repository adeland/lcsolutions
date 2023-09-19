class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        from collections import Counter
        x = Counter(nums)
        return list(x.keys())[list(x.values()).index(max(x.values()))]
