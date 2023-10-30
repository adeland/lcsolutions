class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        count = 0

        if not nums:
            return 0
            
        for element in nums:
            if element - 1 in nums:
                continue
            else:
                while element + 1 in nums:
                    count += 1
                    element += 1
                if count > longest:
                    longest = count
                count = 0

        return longest + 1
