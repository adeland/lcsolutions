class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        ret = 0

        for element in count:

            check = count.get(element)
            if check == 1:
                return - 1
            elif check % 3 == 0:
                ret += check // 3
            else:
                ret += (check // 3) + 1
        
        return ret
        
