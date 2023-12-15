class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = {}
        end = {}

        for cities in paths:
            start[cities[0]] = 0
            end[cities[1]] = 0
            
        for element in end:
            if element not in start:
                return element
    
    
           
