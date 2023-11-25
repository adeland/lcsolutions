class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        left = 0
        total = sum(nums)
        ret = [0] * len(nums) 
        
        for element, num in enumerate(nums):
            ret[element] += element * num - left
            ret[element] += (total - left - num) - (len(nums) - 1 - element) * num
            left += num

        return ret
