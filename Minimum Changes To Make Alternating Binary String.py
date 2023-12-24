class Solution:
    def minOperations(self, s: str) -> int:
        first = 0

        for bit in range(len(s)):
            if bit % 2 == 0 and s[bit] != '0':
                first += 1
            if bit % 2 == 1 and s[bit] != '1': 
                first += 1

        second = 0
        
        for bit in range(len(s)):
            if bit % 2 == 0 and s[bit] != '1':  
                second += 1
            if bit % 2 == 1 and s[bit] != '0': 
                second += 1

        return min(first, second
