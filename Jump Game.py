  class Solution:
    def canJump(self, nums: List[int]) -> bool:
        move = 0

        for jump in nums:
            
            if move < 0:
                return False
            
            elif jump > move:
                move = jump
            move -= 1
        
        return True
