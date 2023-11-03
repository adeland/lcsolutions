class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        count = 1
        length = 0

        while length != len(target):
            stack.append("Push")
            length += 1
            if count != target[length - 1]:
                stack.append("Pop")
                length -= 1
            count += 1

        return stack
            
