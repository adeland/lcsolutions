class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a=set ()
        for ele in nums:
            if ele in a:
                return True
            else:
                a.add(ele)
