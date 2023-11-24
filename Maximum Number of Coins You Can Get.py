class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        current = 0

        while piles:
            piles.pop()
            if piles:
                current += piles[-1]
            piles.pop()
            piles.pop(0)
            
        return current
        
