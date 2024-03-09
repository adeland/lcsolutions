class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        ret = []
        nums1 = set(nums1)
        nums2 = set(nums2)

        for element in nums1:
            if element in nums2:
                ret.append(element)
        ret = sorted(ret)

        if ret:
            return ret[0]
        
        return -1
