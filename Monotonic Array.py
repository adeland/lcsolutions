class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        flag = flag1 = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                flag = False
            elif nums[i] < nums[i + 1]:
                flag1 = False
            if flag == False and flag1 == False:
                return False
        return True

