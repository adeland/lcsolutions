class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        length1 = 0
        length2 = 0

        if left:
            length1 = max(left)
            length1 = n - length1
            length1 = n - length1
        if right:
            length2 = min(right)
            length2 = n - length2
    
        return max(length1, length2)
