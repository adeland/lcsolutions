class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        import itertools
        return set(list(itertools.permutations(nums)))
