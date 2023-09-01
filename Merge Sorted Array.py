class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        count = -1
        for i in nums1:
            count += 1
            if count >= len(nums1) - len(nums2):
                nums1[count] = nums2[0]
                nums2.pop(0)
        nums1.sort()
