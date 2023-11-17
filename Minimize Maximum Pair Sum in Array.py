class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        right = len(nums) - 1
        curr = float('-inf')

        for left in range(len(nums)):
            val = nums[left] + nums[right]
            if val > curr:
                curr = val
            if left == (len(nums) / 2) - 1:
                return curr
            right -= 1
