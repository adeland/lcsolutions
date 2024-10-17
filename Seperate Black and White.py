class Solution:
    def minimumSteps(self, s: str) -> int:
        #Change data type of iteratable structure to a list
        s = list(s)[::-1]
        steps = 0
        curr = 0

        for i in range(len(s)):
            if s[i] == '0':
                curr = i
                break

        for swap in range(curr, len(s)):
            
            if s[swap] == "1":
                #The index of the left most "1"
                steps += swap - curr
                curr += 1
        
        return steps
