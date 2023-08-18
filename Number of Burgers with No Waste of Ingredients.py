class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        """
        :type of cheeseSlices = int
        :type of tomatoSlices = int
        :rtype: List[int]
        
        """
        
        j = tomatoSlices - cheeseSlices * 2
        if j < 0 or j % 2 != 0:
            return []
        
        x= j // 2
        y= cheeseSlices - j // 2
        if x >= 0 and y>=0:
            return [x,y]
        return []
        
