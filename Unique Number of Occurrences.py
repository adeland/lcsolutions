class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen = {}
        checked = Counter(arr)

        for char in checked:
            if checked.get(char) in seen:
                return False
            elif checked.get(char) not in seen:
                seen[checked.get(char)] = 0
                
        return True
