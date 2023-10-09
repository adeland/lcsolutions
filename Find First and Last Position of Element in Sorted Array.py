class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                center = left + (right - left) // 2
                if nums[center] == target:
                    if center == 0 or nums[center - 1] < target:
                        return center
                    right = center - 1
                elif nums[center] < target:
                    left = center + 1
                else:
                    right = center - 1
            return -1
                
        def last(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                center = left + (right - left) // 2
                if nums[center] == target:
                    if center == len(nums) - 1 or nums[center + 1] > target:
                        return center
                    left = center + 1
                elif nums[center] < target:
                    left = center + 1
                else:
                    right = center - 1
            return -1

        return [first(nums, target), last(nums, target)] 
