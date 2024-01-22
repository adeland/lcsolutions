class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        checks = set(nums)
        values = Counter(nums)
        
        for check in list(range(1, len(nums) + 1)):
            if check not in checks:
                error = check
                break

        for check in values:
            if values.get(check) == 2:
                ret = check

        return [ret, error]
