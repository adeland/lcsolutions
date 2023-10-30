class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in strs:
            word = "".join(sorted(i))
            if word not in seen:
                seen[word] = []
            seen[word].append(i)
        return list(seen.values())
