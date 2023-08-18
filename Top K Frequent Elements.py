class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = Counter(nums)
        b = sorted(nums, key = lambda x: (-a[x], x))
        b = list(dict.fromkeys(b))
        return b[0:k]
