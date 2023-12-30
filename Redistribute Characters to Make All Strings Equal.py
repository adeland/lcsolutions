class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        check = ""
      
        for word in words:
            check += word
          
        vals = Counter(check)
      
        for element in vals:
            if vals.get(element) % len(words) != 0:
                return False
              
        return True
