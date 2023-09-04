class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        for i in list(ransomNote):
            if i not in magazine:
                return False
            else:
                magazine.remove(i)
        return True
