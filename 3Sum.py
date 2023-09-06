class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        x = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r = i + 1, len(nums) - 1
            while r > l:
                t = nums[i] + nums[l] + nums[r]
                if t == 0:
                    x.append([nums[i], nums[l], nums[r]])
                    while r > l and nums[l] == nums[l + 1]:
                        l += 1
                    while r > l and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif t < 0:
                    l += 1
                else:
                    r -= 1
        return x
