class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        vals = {}

        for element in range(len(nums)):
            number = nums[element]
            if number in vals and abs(element - vals[number]) <= k:
                return True
            vals[number] = element 
            
        return False
