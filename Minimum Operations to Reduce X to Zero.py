class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        z = sum(nums) - x
        if z == 0:
            return len(nums)
        l, r = 0, 0
        count = 0
        op = float('inf')
        for i in range(len(nums)):
            count += nums[i]
            while count >= z and l < len(nums):
                if count == z:
                    op = min(op, len(nums) - (i - l + 1))
                count -= nums[l]
                l += 1
        return op if op != float('inf') else -1    
# NOT MY SOLUTION
# MY SOLUTION

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        a = 0
        b = 1
        z = sum(nums) - x
        total = 0
        ret = []
        if nums[0] == x:
            return 1
        if nums[-1] == x:
            return 1
        while b != len(nums):
            total = sum(nums[a:b])
            if total == z:
                ret.append(len(nums) - (b - a))
            if total > z:
                total = 0
                a += 1
                b = a
            b += 1
        if ret != []:
            return min(ret)
        return -1
        
