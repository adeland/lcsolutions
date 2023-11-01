class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {"]":"[", ")":"(", "}":"{"}
        
        for element in s:
            if element not in valid:
                stack.append(element)
            else:
                if not stack or stack.pop() != valid.get(element):
                    return False

        return not stack
