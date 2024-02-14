class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        ret = []
        length = len(nums) / 2
        count = 0

        for number in nums:
            
            if number <= 0:
                neg.append(number)
            else:
                pos.append(number)
        
        while length != 0:

            ret.append(pos[count])
            ret.append(neg[count])
            length -= 1
            count += 1
        
        return ret
            
        
        
