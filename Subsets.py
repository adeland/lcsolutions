class Solution:
  import itertools
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub = list(map(lambda x: list(itertools.combinations(nums, x)), range(1, len(nums)+1)))        
        ret = [j for i in sub for j in i]
        ret.append([])
        return ret

        
