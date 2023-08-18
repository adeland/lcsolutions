class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = {}
        for i in strs:
            y = "".join(sorted(i))
            if y in x:
                x[y].append(i)
            else:
                x[y] = [i]
        return list(x.values())
        
