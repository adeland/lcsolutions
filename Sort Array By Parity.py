class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ret = []
        ret1 = []
        for i in nums:
            if i % 2 == 0:
                ret.append(i)
            else:
                ret1.append(i)
        return ret + ret1
