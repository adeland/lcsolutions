class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        x = []
        z = nums.count(target)
        if target not in nums:
            return [-1,-1]
        if z == 1:
            return [nums.index(target),nums.index(target)]
        if z == 2:
            x.append(nums.index(target))
            nums.remove(target)
            x.append(nums.index(target) + 1)
        if z > 2:
            x.append(nums.index(target))
            nums = nums[::-1]
            y = nums.index(target)
            x.append(len(nums) - y - 1)
        return x
