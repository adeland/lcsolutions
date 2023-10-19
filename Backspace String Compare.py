class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        string1 = []
        string2 = []

        for i in s:
            if i != "#":
                string1.append(i)
            if i == "#" and len(string1) >= 1:
                string1.pop()

        for i in t:
            if i != "#":
                string2.append(i)
            if i == "#" and len(string2) >= 1:
                string2.pop()
        
        return string1 == string2
