class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums = set(nums)
        count = 0
        for i in nums:
            if i - 1 not in nums:
                x = i
                y = 1
                while x + 1 in nums:
                    x += 1
                    y += 1
                count = max(count,y)
        return count
