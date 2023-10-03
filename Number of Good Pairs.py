class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in Counter(nums).values():
            i = i * (i - 1) // 2
            count += i
        return count
        
