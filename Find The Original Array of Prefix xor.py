class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        seen = [pref[0]]
        
        if len(pref) == 1:
            return seen

        for i in range(len(pref)):
            if i == len(pref) - 1:
                break
            result = pref[i] ^ pref[i + 1]
            seen.append(result)

        return seen

        
