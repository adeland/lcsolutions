class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        minVal = [0] * len(nums)
        minVal[0] = nums[0]
        for i in range(1, len(nums)):
            minVal[i] = min(minVal[i - 1], nums[i])
        stack = []
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] > minVal[j]:
                while stack and stack[-1] <= minVal[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
        return False
