class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        
        for element in strs:
            word = "".join(sorted(element))
            if word not in seen:
                seen[word] = [] 
            seen[word].append(element)
            
        return list(seen.values())
