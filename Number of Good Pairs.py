class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        from collections import Counter
        x = Counter(nums)
        count = []
        for i in x.values():
            if i > 1:
                z = i
                z = z * (i - 1) // 2
                count.append(z)
        return sum(count)
        
