class Solution:
    def largestGoodInteger(self, num: str) -> str:
        targets = ["999", "888", "777", "666", "555", "444", "333", "222", "111", "000"]
        
        for target in targets:
            if target in num:
                return target
                
        return ""
