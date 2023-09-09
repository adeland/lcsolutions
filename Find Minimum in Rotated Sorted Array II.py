class Solution:
    def findMin(self, nums: List[int]) -> int:
        curr = nums[0]
        for i in nums:
            if i < curr:
                curr = i
        return(curr)
