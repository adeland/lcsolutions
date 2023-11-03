class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        trace = []
        count = 1

        while target != trace:
            trace.append(count)
            stack.append("Push")
            if count not in target:
                trace.pop()
                stack.append("Pop")
            count += 1
            
        return stack
            
