class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        from collections import Counter
        count = 0
        for i in Counter(nums).values():
            if i > 1:
                i = i * (i - 1) // 2
                count += i
        return count
