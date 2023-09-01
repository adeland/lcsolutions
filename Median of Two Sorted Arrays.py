class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        import math
        nums = nums1 + nums2
        nums = sorted(nums)
        z = len(nums)
        if z % 2 == 1:
            y = math.ceil(z/2)
            return nums[y-1]
        else:
            y = nums[int(z/2)] + nums[int((z/2)-1)]
            return y/2
