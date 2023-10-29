class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, element in enumerate(nums):
            value = target - element
            if value in seen:
                return [index, seen.get(value)]
            seen[element] = index
