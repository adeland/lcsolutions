class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret = []

        if len(nums2) >= len(nums1):

            nums1 = set(nums1)
            nums2 = set(nums2)
            for element in nums1:
                if element in nums2:
                    ret.append(element)

        else:

            nums1 = set(nums1)
            nums2 = set(nums2)
            for element in nums2:
                if element in nums1:
                    ret.append(element)

        return ret
